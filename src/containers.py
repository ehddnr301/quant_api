from dependency_injector import containers, providers

from src.repository import (
    UserRepository,
    LimitRepository,
    TransactionRepository,
    AssetRepository,
)
from src.services import UserService, LimitService, TransactionService, AssetService
from src.core.databases import Database


def create_factory(repository_cls, service_cls, session):
    repository = providers.Factory(repository_cls, session=session)
    service = providers.Factory(service_cls, repository=repository)
    return repository, service


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            ".api.user_api",
            ".api.limit_api",
            ".api.transaction_api",
            ".api.asset_api",
        ]
    )

    db = providers.Singleton(Database)

    db_session = providers.Factory(db.provided.session)

    user_repository, user_service = create_factory(
        UserRepository, UserService, db_session
    )
    limit_repository, limit_service = create_factory(
        LimitRepository, LimitService, db_session
    )
    transaction_repository, transaction_service = create_factory(
        TransactionRepository, TransactionService, db_session
    )
    asset_repository, asset_service = create_factory(
        AssetRepository, AssetService, db_session
    )
