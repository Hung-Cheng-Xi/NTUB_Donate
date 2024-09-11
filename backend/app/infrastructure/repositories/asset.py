from sqlmodel import Session, select
from app.domain.models.asset import Asset

class AssetRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_asset(self, asset: Asset):
        """新增一個資產到資料庫"""
        self.session.add(asset)
        self.session.commit()
        self.session.refresh(asset)
        return asset

    def get_asset_by_id(self, asset_id: int):
        """根據資產 ID 取得資產"""
        return self.session.get(Asset, asset_id)

    def get_all_assets(self):
        """取得所有資產"""
        statement = select(Asset)
        results = self.session.exec(statement)
        return results.all()

    def update_asset(self, asset: Asset):
        """更新一個資產"""
        self.session.add(asset)
        self.session.commit()
        self.session.refresh(asset)
        return asset

    def delete_asset(self, asset_id: int):
        """刪除一個資產"""
        asset = self.get_asset_by_id(asset_id)
        if asset:
            self.session.delete(asset)
            self.session.commit()
            return True
        return False
