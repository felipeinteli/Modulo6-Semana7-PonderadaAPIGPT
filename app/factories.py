
class HistoryDAOFactory:
    """
    Creates a dao
    """
    def create(session):
        from .models import HistoryDAO
        return HistoryDAO(session)

