import logging
from app import models


class HistoryServices:

    def create_history(history_map):
        try:
            with models.HistoryDAO() as dao:
                dao.create_history(history_map)
            return True
        except (ValueError, TypeError) as e:
            return False
        except Exception as e:
            return False
        
    def find_all(self):
        try:
            with models.HistoryDAO() as dao:
                result = dao.find_all()
            return result
        except Exception as e:
            return []

