
from typing import TYPE_CHECKING, Any, Dict, List, Tuple

if TYPE_CHECKING:
    from _typeshed import FileDescriptorLike
    from feishu.api import OpenLark
    from six import string_types


class APIBitableMixin(object):
    def get_bitable_records(self, app_token, table_id, query=''):
        url = self._gen_request_url(
            "/open-apis/bitable/v1/apps/{}/tables/{}/records{}".format(
                app_token,
                table_id,
                query
            )
        )
        res = self._get(url, with_tenant_token=True, success_code=0)
        return res.get('data')

    def select_bitable_record(self, app_token, table_id, record_id):
        url = self._gen_request_url(
            '/open-apis/bitable/v1/apps/{}/tables/{}/records/{}'.format(
                app_token,
                table_id,
                record_id
            )
        )
        res = self._get(url, with_tenant_token=True, success_code=0)
        return res.get('data')

    def add_bitable_record(self, app_token, table_id, record):
        url = self._gen_request_url(
            '/open-apis/bitable/v1/apps/{}/tables/{}/records'.format(
                app_token,
                table_id
            )
        )
        body = dict(fields = record)
        res = self._post(url, body, with_tenant_token=True, success_code=0)
        return res.get('data')
    
    def batch_add_bitable_records(self, app_token, table_id, records):
        url = self._gen_request_url(
            '/open-apis/bitable/v1/apps/{}/tables/{}/records/batch_create'.format(
                app_token,
                table_id
            )
        )
        if (records):
            body = dict(records = records)
            res = self._post(url, body, with_tenant_token=True, success_code=0)
            return res.get('data')

    def update_bitable_record(self, app_token, table_id, record_id, record):
        url = self._gen_request_url(
            '/open-apis/bitable/v1/apps/{}/tables/{}/records/{}'.format(
                app_token,
                table_id,
                record_id
            )
        )
        body = dict(fields = record)
        res = self._put(url, body, with_tenant_token=True, success_code=0)
        return res.get('data')
    
    def batch_update_bitable_records(self, app_token, table_id, records):
        url = self._gen_request_url(
            '/open-apis/bitable/v1/apps/{}/tables/{}/records/batch_update'.format(
                app_token,
                table_id
            )
        )
        if (records):
            body = dict(records = records)
            res = self._post(url, body, with_tenant_token=True, success_code=0)
            return res.get('data')
        

    def delete_bitable_record(self, app_token, table_id, record_id):
        url = self._gen_request_url(
            '/open-apis/bitable/v1/apps/{}/tables/{}/records/{}'.format(
                app_token,
                table_id,
                record_id
            )
        )
        res = self._delete(url, with_tenant_token=True, success_code=0)
        return res.get('data')

    def batch_delete_bitable_records(self, app_token, table_id, record_ids):
        url = self._gen_request_url(
            '/open-apis/bitable/v1/apps/{}/tables/{}/records/batch_delete'.format(
                app_token,
                table_id,
            )
        )
        if (record_ids):
            body = dict(records = record_ids)
            res = self._post(url, body, with_tenant_token=True, success_code=0)
            return res.get('data')
