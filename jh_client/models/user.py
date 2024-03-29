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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from jh_client.models.server import Server
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class User(BaseModel):
    """
    User
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The user's name")
    admin: Optional[StrictBool] = Field(default=None, description="Whether the user is an admin")
    roles: Optional[List[StrictStr]] = Field(default=None, description="The names of roles this user has")
    groups: Optional[List[StrictStr]] = Field(default=None, description="The names of groups where this user is a member")
    server: Optional[StrictStr] = Field(default=None, description="The user's notebook server's base URL, if running; null if not.")
    pending: Optional[StrictStr] = Field(default=None, description="The currently pending action, if any")
    last_activity: Optional[datetime] = Field(default=None, description="Timestamp of last-seen activity from the user")
    servers: Optional[Dict[str, Server]] = Field(default=None, description="The servers for this user. By default: only includes _active_ servers. Changed in 3.0: if `?include_stopped_servers` parameter is specified, stopped servers will be included as well. ")
    auth_state: Optional[Dict[str, Any]] = Field(default=None, description="Authentication state of the user. Only available with admin:users:auth_state scope. None otherwise. ")
    __properties: ClassVar[List[str]] = ["name", "admin", "roles", "groups", "server", "pending", "last_activity", "servers", "auth_state"]

    @field_validator('pending')
    def pending_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('spawn', 'stop'):
            raise ValueError("must be one of enum values ('spawn', 'stop')")
        return value

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
        """Create an instance of User from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in servers (dict)
        _field_dict = {}
        if self.servers:
            for _key in self.servers:
                if self.servers[_key]:
                    _field_dict[_key] = self.servers[_key].to_dict()
            _dict['servers'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "admin": obj.get("admin"),
            "roles": obj.get("roles"),
            "groups": obj.get("groups"),
            "server": obj.get("server"),
            "pending": obj.get("pending"),
            "last_activity": obj.get("last_activity"),
            "servers": dict(
                (_k, Server.from_dict(_v))
                for _k, _v in obj.get("servers").items()
            )
            if obj.get("servers") is not None
            else None,
            "auth_state": obj.get("auth_state")
        })
        return _obj


