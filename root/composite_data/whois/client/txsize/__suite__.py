name = "transaction size"

graph_size = [pow(2,17)]
description = "Ingest as a function of transaction size (graph size {0}).".format(graph_size)

tx_sizes = []
for i in xrange(4,17):
    tx_sizes.append(pow(2,i))
    pass
tx_sizes.reverse()
table_view = [
    [{"sTitle":"Platform"},{"content":"object.platform()"}],
    [{"sTitle":"Transaction Size"},{"content":"object.tx_size()"}],
    [{"sTitle":"Rate (v/s)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}]
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","math.log(object.tx_size(),2)"),"xaxis":"pow(2,Transaction size)"},
        {"name":"time","data":("object.time_avg()*0.001","math.log(object.tx_size(),2)"),"xaxis":"pow(2,Transaction size)"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        ]
}

cases = [
    {
        "name":"pipeline.client.submit",
        "description":"Composite Ingest as a function of transaction size (page_size=%d)."%(pow(2,14)),
        "type":"pipeline_composite_ingest",
        "data":
        {
            "composite_name":"BaseModel",
            "template":["whois"],
            "config":["default:default"],
            "page_size":[14],
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
    ]

    


    




    
