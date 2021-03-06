
from typing import TYPE_CHECKING, Any, Dict, List, Tuple

if TYPE_CHECKING:
    from feishu.api import OpenLark
    from six import string_types


class APIBitableMixin(object):
    def get_bitable_records(self, app_token, table_id):
        url = self._gen_request_url(
            '/open-apis/bitable/v1/apps/{}/tables/{}/records'.format(
                app_token,
                table_id
            )
        )
        res = self._get(url, with_tenant_token=True, success_code=0)
        return res.get("data")

    def add_bitable_record(self, app_token, table_id, records):
        url = self._gen_request_url(
            '/open-apis/bitable/v1/apps/{}/tables/{}/records/batch_create'.format(
                app_token,
                table_id
            )
        )
        res = self._post(url, records, with_tenant_token=True, success_code=0)
        return res.get("data")

    def update_bitable_record():
        pass

    def delete_bitable_record():
        pass
