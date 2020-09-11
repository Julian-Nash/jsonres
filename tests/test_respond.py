from flask import Blueprint, Flask
from respond import Responder
from respond.abs_http_response import HTTPResponse

from typing import Optional, Any
from http import HTTPStatus
import unittest
import json


json_bp: Blueprint = Blueprint("json", __name__, url_prefix="/json")
http_bp: Blueprint = Blueprint("http", __name__, url_prefix="/http")
xml_bp: Blueprint = Blueprint("xml", __name__, url_prefix="/xml")
headers_bp : Blueprint = Blueprint("headers", __name__, url_prefix="/headers")
text_bp : Blueprint = Blueprint("text", __name__, url_prefix="/text")

xml_test_data: str = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>http://www.example.com/</loc>
      <lastmod>2005-01-01</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
   </url>
</urlset>"""


@json_bp.route("")
def json_ok():
    return Responder.json.ok()


@json_bp.route("/headers")
def json_custom_headers():
    return Responder.json.ok(headers={"X-Custom": "OK"})


@json_bp.route("/str")
def json_str():
    return Responder.json.ok("Test OK")


@json_bp.route("/int")
def json_int():
    return Responder.json.ok(1)


@json_bp.route("/float")
def json_float():
    return Responder.json.ok(1.1)


@json_bp.route("/list")
def json_list():
    return Responder.json.ok([1, 2, 3])


@json_bp.route("/dict")
def json_dict():
    return Responder.json.ok({"test": {"data": [1, 2, 3]}})


@json_bp.route("/none")
def json_none():
    return Responder.json.ok(None)


# HTTP Blueprint


@http_bp.route("/100")
def continue_():
    return Responder.text.continue_()


@http_bp.route("/101")
def switching_protocols():
    return Responder.text.switching_protocols()


@http_bp.route("/102")
def processing():
    return Responder.text.processing()


@http_bp.route("/200")
def ok():
    return Responder.text.ok()


@http_bp.route("/201")
def created():
    return Responder.text.created()


@http_bp.route("/202")
def accepted():
    return Responder.text.accepted()


@http_bp.route("/203")
def non_authoritative_information():
    return Responder.text.non_authoritative_information()


@http_bp.route("/204")
def no_content():
    return Responder.text.no_content()


@http_bp.route("/205")
def reset_content():
    return Responder.text.reset_content()


@http_bp.route("/206")
def partial_content():
    return Responder.text.partial_content()


@http_bp.route("/207")
def multi_status():
    return Responder.text.multi_status()


@http_bp.route("/208")
def already_reported():
    return Responder.text.already_reported()


@http_bp.route("/226")
def im_used():
    return Responder.text.im_used()


@http_bp.route("/300")
def multiple_choices():
    return Responder.text.multiple_choices()


@http_bp.route("/301")
def moved_permanently():
    return Responder.text.moved_permanently()


@http_bp.route("/302")
def found():
    return Responder.text.found()


@http_bp.route("/303")
def see_other():
    return Responder.text.see_other()


@http_bp.route("/304")
def not_modified():
    return Responder.text.not_modified()


@http_bp.route("/305")
def use_proxy():
    return Responder.text.use_proxy()


@http_bp.route("/307")
def temporary_redirect():
    return Responder.text.temporary_redirect()


@http_bp.route("/308")
def permanent_redirect():
    return Responder.text.permanent_redirect()


@http_bp.route("/400")
def bad_request():
    return Responder.text.bad_request()


@http_bp.route("/401")
def unauthorized():
    return Responder.text.unauthorized()


@http_bp.route("/402")
def payment_required():
    return Responder.text.payment_required()


@http_bp.route("/403")
def forbidden():
    return Responder.text.forbidden()


@http_bp.route("/404")
def not_found():
    return Responder.text.not_found()


@http_bp.route("/405")
def method_not_allowed():
    return Responder.text.method_not_allowed()


@http_bp.route("/406")
def not_acceptable():
    return Responder.text.not_acceptable()


@http_bp.route("/407")
def proxy_authentication_required():
    return Responder.text.proxy_authentication_required()


@http_bp.route("/408")
def request_timeout():
    return Responder.text.request_timeout()


@http_bp.route("/409")
def conflict():
    return Responder.text.conflict()


@http_bp.route("/410")
def gone():
    return Responder.text.gone()


@http_bp.route("/411")
def length_required():
    return Responder.text.length_required()


@http_bp.route("/412")
def precondition_failed():
    return Responder.text.precondition_failed()


@http_bp.route("/413")
def request_entity_too_large():
    return Responder.text.request_entity_too_large()


@http_bp.route("/414")
def request_uri_too_long():
    return Responder.text.request_uri_too_long()


@http_bp.route("/415")
def unsupported_media_type():
    return Responder.text.unsupported_media_type()


@http_bp.route("/416")
def requested_range_not_satisfiable():
    return Responder.text.requested_range_not_satisfiable()


@http_bp.route("/417")
def expectation_failed():
    return Responder.text.expectation_failed()


@http_bp.route("/421")
def misdirected_request():
    return Responder.text.misdirected_request()


@http_bp.route("/422")
def unprocessable_entity():
    return Responder.text.unprocessable_entity()


@http_bp.route("/423")
def locked():
    return Responder.text.locked()


@http_bp.route("/424")
def failed_dependency():
    return Responder.text.failed_dependency()


@http_bp.route("/426")
def upgrade_required():
    return Responder.text.upgrade_required()


@http_bp.route("/428")
def precondition_required():
    return Responder.text.precondition_required()


@http_bp.route("/429")
def too_many_requests():
    return Responder.text.too_many_requests()


@http_bp.route("/431")
def request_header_fields_too_large():
    return Responder.text.request_header_fields_too_large()


@http_bp.route("/451")
def unavailable_for_legal_reasons():
    return Responder.text.unavailable_for_legal_reasons()


@http_bp.route("/500")
def internal_server_error():
    return Responder.text.internal_server_error()


@http_bp.route("/501")
def not_implemented():
    return Responder.text.not_implemented()


@http_bp.route("/502")
def bad_gateway():
    return Responder.text.bad_gateway()


@http_bp.route("/503")
def service_unavailable():
    return Responder.text.service_unavailable()


@http_bp.route("/504")
def gateway_timeout():
    return Responder.text.gateway_timeout()


@http_bp.route("/505")
def http_version_not_supported():
    return Responder.text.http_version_not_supported()


@http_bp.route("/506")
def variant_also_negotiates():
    return Responder.text.variant_also_negotiates()


@http_bp.route("/507")
def insufficient_storage():
    return Responder.text.insufficient_storage()


@http_bp.route("/508")
def loop_detected():
    return Responder.text.loop_detected()


@http_bp.route("/510")
def not_extended():
    return Responder.text.not_extended()


@http_bp.route("/511")
def network_authentication_required():
    return Responder.text.network_authentication_required()


# Headers blueprint


@headers_bp.route("")
def headers():
    return Responder.text.ok(headers={"X-Foo": "Bar", "X-Bar": "Baz"})


# Text blueprint


@text_bp.route("")
def text():
    return Responder.text.ok()


@text_bp.route("/content")
def text_content():
    return Responder.text.ok("Test OK")


# XML blueprint


@xml_bp.route("")
def xml():
    return Responder.xml.ok(xml_test_data)


@xml_bp.route("/headers")
def xml_headers():
    return Responder.xml.ok(xml_test_data, headers={"X-Custom": "xml"})


def create_app() -> Flask:

    app = Flask(__name__)

    for bp in [http_bp, json_bp, headers_bp, text_bp, xml_bp]:
        app.register_blueprint(bp)

    return app


class TestRespondExtendingHTTPResponseBaseClass(unittest.TestCase):

    def setUp(self) -> None:
        app = create_app()
        self.test_client = app.test_client()

    def test_not_implemented_error(self):

        class CustomHTTPResponse(HTTPResponse):
            ...

        with self.assertRaises(NotImplementedError):
            data = CustomHTTPResponse.ok()

    def test_http_response_subclassed(self):

        class CustomHTTPResponse(HTTPResponse):

            @classmethod
            def _make_response(cls, status: int, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
                return "CUSTOM OK"

        self.assertEqual(CustomHTTPResponse.ok(), "CUSTOM OK")


class TestRespondHTTPStatus(unittest.TestCase):

    def setUp(self) -> None:
        app = create_app()
        self.test_client = app.test_client()

    def test_http_status_codes(self):

        for status in HTTPStatus:
            r = self.test_client.get(f"/http/{status}")
            self.assertEqual(r.status_code, status)


class TestRespondJSONResponse(unittest.TestCase):

    def setUp(self) -> None:
        app = create_app()
        self.test_client = app.test_client()

    def _load_json(self, s: str):
        return json.loads(s)

    def test_json_content_type_header(self):

        r = self.test_client.get("/json")
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertEqual(r.content_type, "application/json")

    def test_json_custom_header(self):

        r = self.test_client.get("/json/headers")
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertEqual(r.headers["X-Custom"], "OK")

    def test_json_ok(self):

        r = self.test_client.get("/json")
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertEqual(self._load_json(r.data), "")

    def test_json_str(self):

        r = self.test_client.get("/json/str")
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertEqual(self._load_json(r.data), "Test OK")

    def test_json_int(self):

        r = self.test_client.get("/json/int")
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertEqual(self._load_json(r.data), 1)

    def test_json_float(self):

        r = self.test_client.get("/json/float")
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertEqual(self._load_json(r.data), 1.1)

    def test_json_list(self):

        r = self.test_client.get("/json/list")
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertEqual(self._load_json(r.data), [1, 2, 3])

    def test_json_dict(self):

        r = self.test_client.get("/json/dict")
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertEqual(self._load_json(r.data), {"test": {"data": [1, 2, 3]}})

    def test_json_none(self):

        r = self.test_client.get("/json/none")
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertEqual(self._load_json(r.data), "")


class TestRespondHeaders(unittest.TestCase):

    def setUp(self) -> None:
        app = create_app()
        self.test_client = app.test_client()

    def test_headers(self):

        r = self.test_client.get("/headers")
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertEqual(r.headers["X-Foo"], "Bar")
        self.assertEqual(r.headers["X-Bar"], "Baz")


class TestRespondText(unittest.TestCase):

    def setUp(self) -> None:
        app = create_app()
        self.test_client = app.test_client()

    def test_text_content_type(self):

        r = self.test_client.get("/text")
        self.assertEqual(r.content_type, "text/plain; charset=utf-8")
        self.assertEqual(r.status_code, HTTPStatus.OK)

    def test_text_content(self):

        r = self.test_client.get("/text/content")
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertEqual(r.data.decode(), "Test OK")


class TestRespondXML(unittest.TestCase):

    def setUp(self) -> None:
        app = create_app()
        self.test_client = app.test_client()

    def test_xml_content_type(self):

        r = self.test_client.get("/xml")
        self.assertEqual(r.content_type, "text/xml; charset=utf-8")
        self.assertEqual(r.status_code, HTTPStatus.OK)

    def test_xml_headers(self):
        r = self.test_client.get("/xml/headers")
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertEqual(r.headers["X-Custom"], "xml")

    def test_xml_content(self):
        r = self.test_client.get("/xml")
        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertEqual(r.data.decode(), xml_test_data)
