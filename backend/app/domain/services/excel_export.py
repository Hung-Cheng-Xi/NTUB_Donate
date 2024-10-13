import pandas as pd
from io import BytesIO
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from typing import Annotated
from fastapi import Depends

from app.core.database import get_db_session
from app.application.client.schemas.unit import UnitInfo
from app.application.client.schemas.donation import DonationInfo
from app.application.client.schemas.donation_purpose import DonationPurposeInfo
from app.domain.models.unit import Unit
from app.domain.models.donation import Donations
from app.domain.models.donation_purpose import DonationPurpose


class ExcelService:
    def __init__(
        self,
        session: Annotated[AsyncSession, Depends(get_db_session)]
    ):
        self.session = session

    async def fetch_data(self):
        """從資料庫中獲取捐款記錄、捐款目的及受捐單位資料"""

        statement = (
            select(Donations, DonationPurpose, Unit)
            .join(DonationPurpose, Donations.purpose_id == DonationPurpose.id)
            .join(Unit, DonationPurpose.unit_id == Unit.id)
        )
        result = await self.session.execute(statement)
        return result.all()

    def transform_to_dict(self, donation, purpose, unit):
        """將資料轉換為字典格式，用於創建 DataFrame"""

        donation_info = DonationInfo.model_validate(donation)
        purpose_info = DonationPurposeInfo.model_validate(
            purpose) if purpose else None
        unit_info = UnitInfo.model_validate(unit) if unit else None

        return {
            "編號": donation_info.id,
            "受捐單位": unit_info.name if unit_info else "N/A",
            "捐款名義": purpose_info.name if purpose_info else "N/A",
            "捐款金額": donation_info.amount,
            "捐款方式": donation_info.type.value,
            "捐款人姓名(公司名稱)": donation_info.username,
            "身分證字號(統一編號)": donation_info.id_card,
            "生日": donation_info.user_birthday,
            "聯絡電話(行動電話)": donation_info.phone_number,
            "email信箱": donation_info.email,
            "捐款人身分": donation_info.identity.value,
            "畢業年": donation_info.year,
            "學制/科/系/所": donation_info.gept,
            "戶籍地址": donation_info.registered_address,
            "通訊地址": donation_info.res_address,
            "公開資訊": donation_info.public_status,
            "備註": donation_info.memo,
            "繳費單代碼": donation_info.account,
            "繳款日期": donation_info.input_date,
        }

    async def create_workbook(self):
        """創建一個包含捐款資料的 DataFrame"""

        # 獲取資料
        records = await self.fetch_data()

        # 將資料轉換為字典列表
        data = [
            self.transform_to_dict(donation, purpose, unit)
            for donation, purpose, unit in records
        ]

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
