from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.domain.models.asset import asset


class assetRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_asset(self, new_asset: asset):
        """新增一個資產到資料庫"""
        self.session.add(new_asset)
        await self.session.commit()
        await self.session.refresh(new_asset)
        return new_asset

    async def get_asset_by_id(self, asset_id: int):
        """根據資產 ID 取得資產"""
        result = await self.session.get(asset, asset_id)
        return result

    async def get_all_assets(self):
        """取得所有資產"""
        statement = select(asset)
        results = await self.session.execute(statement)
        return results.scalars().all()

    async def update_asset(self, updated_asset: asset):
        """更新一個資產"""
        self.session.add(updated_asset)
        await self.session.commit()
        await self.session.refresh(updated_asset)
        return updated_asset

    async def delete_asset(self, asset_id: int):
        """刪除一個資產"""
        asset_to_delete = await self.get_asset_by_id(asset_id)
        if asset_to_delete:
            await self.session.delete(asset_to_delete)
            await self.session.commit()
            return True
        return False
