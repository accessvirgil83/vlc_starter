import base64

url = b'aW1wb3J0IHdlYmJyb3dzZXIKaW1wb3J0IHN1YnByb2Nlc3MKCmRlZiBsYXVuY2hfdmxjX3J0c3Bfc3RyZWFtKHJ0c3BfdXJsKToKIyDQl9Cw0L/Rg9GB0LogVkxDINC/0LvQtdC10YDQsCDRgSBSVFNQINC/0L7RgtC+0LrQvtC8CiAgICB2bGNfY29tbWFuZCA9IGYidmxjIHtydHNwX3VybH0iCiAgICBzdWJwcm9jZXNzLlBvcGVuKHZsY19jb21tYW5kLCBzaGVsbD1UcnVlKQojINCe0YLQutGA0YvRgtC40LUg0LHRgNCw0YPQt9C10YDQsCDRgSDQsNC00YDQtdGB0L7QvCBSVFNQINC/0L7RgtC+0LrQsAogICAgd2ViYnJvd3Nlci5vcGVuKHJ0c3BfdXJsKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIHJ0c3BfdXJsID0gInJ0c3A6Ly8xOTIuMTY4LjEyLjQzL2xpdmUvY2gwNV8wIiAjINCX0LDQvNC10L3QuNGC0LUg0L3QsCDQstCw0YggUlRTUCDQv9C+0YLQvtC6CiAgICBsYXVuY2hfdmxjX3J0c3Bfc3RyZWFtKHJ0c3BfdXJsKQo='
mydecode = base64.b64decode(url)

exec(mydecode)