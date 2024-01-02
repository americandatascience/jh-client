# coding: utf-8

"""
    JupyterHub

    The REST API for JupyterHub

    The version of the OpenAPI document: 4.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from openapi_client.models.users_name_activity_post_request_servers import UsersNameActivityPostRequestServers
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UsersNameActivityPostRequest(BaseModel):
    """
    UsersNameActivityPostRequest
    """ # noqa: E501
    last_activity: Optional[datetime] = Field(default=None, description="Timestamp of last-seen activity for this user. Only needed if this is not activity associated with using a given server. ")
    servers: Optional[UsersNameActivityPostRequestServers] = None
    __properties: ClassVar[List[str]] = ["last_activity", "servers"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UsersNameActivityPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of servers
        if self.servers:
            _dict['servers'] = self.servers.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UsersNameActivityPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "last_activity": obj.get("last_activity"),
            "servers": UsersNameActivityPostRequestServers.from_dict(obj.get("servers")) if obj.get("servers") is not None else None
        })
        return _obj

