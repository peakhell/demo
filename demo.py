import webbrowser
import json


def plot_net(graph, filename):
    with open("plot.js", "r") as f:
        data_func = f.read()
    with open(filename, "w") as f:
        f.write(''.join([
            '<html>',
            '<head><meta charset="utf-8" /></head>',
            "<script src='https://d3js.org/d3.v4.min.js'></script>",
            "<link href='demo.css' rel='stylesheet' type='text/css'/>",
            '<body>',
            "<div id='draw'>",
            "<svg></svg>",
            "</div>"
            "<script>",
            data_func,
            "read_data({});".format(graph),
            "</script>"
        ]))
    webbrowser.open_new_tab(filename)


if __name__ == "__main__":
    # 在python中打开一个json文件
    graph = json.loads(open("demo.json", "r").read())

    # 绘图并打开一个html文件
    plot_net(graph, "net.html")
