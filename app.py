from dash import *
from testapp import *

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    github_info_header(),
    html.Img(src="assets/cute_ferret.jpeg"),
    html.Div(children='done well!!!'),
])

if __name__ == '__main__':
    app.run_server(debug=True)






