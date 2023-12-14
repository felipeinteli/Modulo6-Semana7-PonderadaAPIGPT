import json
import logging

from .factories import *
from .dao import BaseDAO
from .entitie import *


# SERVIÇO CHAMA 
""" DAO
================================================================================
"""

class HistoryDAO(BaseDAO):

    def create_history(self, map_):
        """
        Add a history to the Database
        """
        #logging.error(f"entrou create_history dao")
        entity = HistoryEntity(
            prompt = map_['prompt'],
            resposta = map_['resposta']

        )
        logging.error(entity)
        return self._session.add(entity)
    
    
    def find_all(self):
        entities = self.find_all_entity()
        return self._build_models_from_entities(entities)
    

    def find_all_entity(self):
        return self._session.query(HistoryEntity).all()
    
    def _build_model_from_entity(self, entity):
        """
        Build a Student model out of an entity
        """
        history = History(
            id = entity.id,
            prompt = entity.prompt,
            resposta = entity.resposta
        )
        return history
    
    def _build_models_from_entities(self, entities):
        historys = []
        for entity in entities:
            historys.append(self._build_model_from_entity(entity))
        return historys
    


""" Model
================================================================================
"""

class History:

    def __init__(self, id, prompt, resposta):
        self._id = id
        self._prompt = prompt
        self._resposta = resposta

    @property
    def id(self):
        return self._id

    def add_id(self, id):
        self._id = id

    @property
    def prompt(self):
        return self._prompt
    
    @property
    def add_prompt(self, prompt):
        self._prompt = prompt
    
    @property
    def resposta(self):
        return self._resposta
    
    @property
    def add_resposta(self, resposta):
        self._resposta = resposta
    

    def jsonify(self, indent=2):
        map_ = self.to_map()
        # map_["status"] = self.status().to_dict()
        # for key, value in map_.items():
        #     if isinstance(value, datetime):
        #         map_[key] = value.isoformat()
        #     elif isinstance(value, str):
        #         map_[key] = value.encode('utf-8').decode('utf-8')
        return json.dumps(map_, indent=indent, ensure_ascii=False)

    def to_map(self):
        return {
            "id": self._id,
            "prompt": self._prompt,
            "resposta": self._resposta
        }