from typing import Annotated
from openpyxl import Workbook
from io import BytesIO
from fastapi import Depends
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db_session
from app.application.client.schemas.unit import UnitInfo
from app.application.client.schemas.donation import DonationInfo
from app.application.client.schemas.donation_purpose import DonationPurposeInfo
from app.domain.models.unit import Unit
from app.domain.models.donation import Donations
from app.domain.models.donation_purpose import DonationPurpose


class ExcelService:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_db_session)]):
        self.session = session

    async def create_workbook(self):
        # 創建一個新的工作簿
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Data"

        # 添加標題行
        headers = [
            "編號", "受捐單位", "捐款名義", "捐款金額", "捐款方式", "捐款人姓名(公司名稱)", "身分證字號(統一編號)", "生日",
            "聯絡電話(行動電話)", "email信箱", "捐款人身分", "畢業年", "學制/科/系/所", "戶籍地址", "通訊地址", "公開資訊",
            "備註", "繳費單代碼", "繳款日期"
        ]
        sheet.append(headers)

        # 使用 JOIN 獲取數據
        statement = (
            select(Donations, DonationPurpose, Unit)
            .join(DonationPurpose, Donations.purpose_id == DonationPurpose.id)
            .join(Unit, DonationPurpose.unit_id == Unit.id)
        )
        result = await self.session.execute(statement)
        records = result.all()

        # 填充表格數據
        for donation, purpose, unit in records:
            donation_info = DonationInfo.model_validate(donation)
            purpose_info = DonationPurposeInfo.model_validate(
                purpose) if purpose else None
            unit_info = UnitInfo.model_validate(unit) if unit else None

            row = [
                donation_info.id, unit_info.name if unit_info else "N/A", purpose_info.name, donation_info.amount, donation_info.type.value, donation_info.username,
                donation_info.id_card, donation_info.user_birthday, donation_info.phone_number, donation_info.email, donation_info.identity.value,
                donation_info.year, donation_info.gept, donation_info.registered_address, donation_info.res_address, donation_info.public_status,
                donation_info.memo, donation_info.account, donation_info.input_date
            ]
            sheet.append(row)

        return workbook

    async def export_to_bytes(self, workbook):
        # 將工作簿儲存到內存中的 BytesIO
        output = BytesIO()
        workbook.save(output)
        output.seek(0)
        return output
