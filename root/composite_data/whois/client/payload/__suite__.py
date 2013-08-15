name = "payload"

graph_size = [pow(2,12)]
description = "Ingest as a function of page size (graph size {0}).".format(graph_size)

tx_sizes = [pow(2,7)]
page_sizes = [16,15,14,13,12,11,10]
table_view = [
    [{"sTitle":"Platform"},{"content":"object.platform()"}],
    [{"sTitle":"Page Size"},{"content":"object.page_size()"}],
    [{"sTitle":"Rate (ops/sec)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}]
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","object.page_size()"),"xaxis":"pow(2,Page size)"},
        {"name":"time","data":("object.time_avg()*0.001","object.page_size()"),"xaxis":"pow(2,Page size)"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        ]
}
cases = []

for model in ("BaseModel.1","BaseModel.2","BaseModel.3","BaseModel.4"):
    cases.append(
        {
            "name":"submit.{0}".format(model),
            "description":"Composite Ingest as a function of page size (transaction size = {0}) (model = {1})".format(tx_sizes,model),
            "type":"pipeline_composite_ingest",
            "data":
            {
                "composite_name":model,
                "template":["whois"],
                "config":["default:default"],
                "page_size":page_sizes,
                "threads":[1],
                "use_index":[1],
                "new":1,
                "size":graph_size,
                "txsize":tx_sizes,
                "ig_version":["ig.3.1.task"]
                },
            "table_view":table_view,
            "plot_view":plot_view
            }
        )
    pass

