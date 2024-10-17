import pandas as pd

from io import BytesIO
from typing import Annotated, Dict, List

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.application.admin.schemas.donation import ExcelExportInfo
from app.infrastructure.repositories.donation import DonationRepository


class ExcelService:
    def __init__(
        self,
        session: Annotated[AsyncSession, Depends(get_db_session)],
        donation_repository: Annotated[DonationRepository, Depends()]
    ):
        self.session = session
        self.donation_repository = donation_repository

    def transform_to_dict(
        self,
        export_data: List[ExcelExportInfo],
    ) -> Dict:
        """將資料轉換為字典格式，用於創建 DataFrame"""

        transformed_data = []

        for data in export_data:
            transformed_data.append({
                "編號": data.id,
                "受捐單位": data.purpose.unit.name if data.purpose.unit else "N/A",
                "捐款名義": data.purpose.title if data.purpose else "N/A",
                "捐款金額": data.amount,
                "捐款方式": data.type.value,
                "捐款人姓名(公司名稱)": data.username,
                "身分證字號(統一編號)": data.id_card,
                "生日": data.user_birthday,
                "聯絡電話(行動電話)": data.phone_number,
                "email信箱": data.email,
                "捐款人身分": data.identity.value,
                "畢業年": data.year,
                "學制/科/系/所": data.gept,
                "戶籍地址": data.registered_address,
                "通訊地址": data.res_address,
                "公開資訊": data.public_status.value,
                "備註": data.memo,
                "繳費單代碼": data.account,
                "繳款日期": data.input_date,
            })

        return transformed_data

    async def create_workbook(
        self,
        skip: int,
        limit: int
    ):
        """創建一個包含捐款資料的 DataFrame"""

        # 獲取資料
        records = await self.donation_repository.export_excel(skip, limit)

        # 將資料轉換為字典列表
        export_data = [
            ExcelExportInfo.model_validate(record)
            for record in records
        ]

        data = self.transform_to_dict(export_data)

        # 創建 DataFrame
        df = pd.DataFrame(data)
        return df

    async def export_to_bytes(self, df: pd.DataFrame):
        """將 DataFrame 匯出為 Excel 文件並儲存到 BytesIO"""

        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name="Data")
        output.seek(0)
        return output
