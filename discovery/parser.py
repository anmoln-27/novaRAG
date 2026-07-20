import requests


class DiscoveryEngine:

    def __init__(self):
        self.base_url = "http://127.0.0.1:8080"

    def discover_routes(self):

        response = requests.get(
            f"{self.base_url}/openapi.json"
        )

        spec = response.json()

        paths = spec.get("paths", {})
        schemas = spec.get("components", {}).get("schemas", {})

        endpoints = []

        for path, methods in paths.items():

            if path.startswith("/docs") or \
               path.startswith("/redoc") or \
               path.startswith("/openapi"):
                continue

            for method, details in methods.items():

                endpoint = {
                    "path": path,
                    "method": method.upper(),
                    "summary": details.get("summary", ""),
                    "fields": {}
                }

                # Extract request body schema
                request_body = details.get("requestBody")

                if request_body:

                    content = request_body.get("content", {})

                    json_schema = content.get("application/json", {})

                    schema = json_schema.get("schema", {})

                    ref = schema.get("$ref")

                    if ref:

                        schema_name = ref.split("/")[-1]

                        schema_obj = schemas.get(schema_name, {})

                        props = schema_obj.get("properties", {})

                        for name, value in props.items():

                            endpoint["fields"][name] = value.get("type", "unknown")

                endpoints.append(endpoint)

        return endpoints