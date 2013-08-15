name = "processes"

graph_size = pow(2,13)
description = "Ingest as a function of threads (graph size {0})).".format(graph_size)
threads = [1]
processes = [(None,1),(None,2),(None,3),(None,4),(None,5),(None,6),(None,7)]
tx_sizes = [pow(2,13)]
page_sizes = [13]
table_view = [
    [{"sTitle":"Platform"},{"content":"object.platform()"}],
    [{"sTitle":"Processes"},{"content":"object.processes()"}],
    [{"sTitle":"Rate (v/s)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}]
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","object.processes()"),"xaxis":"processes"},
        {"name":"time","data":("object.time_avg()*0.001","object.processes()"),"xaxis":"processes"},
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
            "page_size":page_sizes,
            "threads":threads,
            "process":processes,            
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



    


    




    
