name = "threaded"

graph_size = pow(2,13)*4
description = "Ingest as a function of threads (graph size {0})).".format(graph_size)
threads = [1,2,3,4]
tx_sizes = [pow(2,13)]
table_view = [
    [{"sTitle":"Platform"},{"content":"object.platform()"}],
    [{"sTitle":"Threads"},{"content":"object.threads()"}],
    [{"sTitle":"Rate (v/s)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}]
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","object.threads()"),"xaxis":"threads"},
        {"name":"time","data":("object.time_avg()*0.001","object.threads()"),"xaxis":"threads"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        ]
}

cases = []
cases = [
    {
        "name":"pipeline.client.submit",
        "description":"Composite Ingest as a function of threads",
        "type":"pipeline_composite_ingest",
        "data":
        {
            "composite_name":"BaseModel",
            "template":["whois"],
            "config":["default:default"],
            "page_size":[13],
            "threads":threads,
            "use_index":[1],
            "new":1,
            "size":[graph_size],
            "txsize":tx_sizes,
            "ig_version":["ig.3.1.task"]
            },
        "table_view":table_view,
        "plot_view":plot_view
        }
    ]



    


    




    
