name = "disks"

graph_size = pow(2,17)
description = "Ingest as a function of processes and disks (graph size {0})).".format(graph_size)
threads = [1]
processes = []
for i in [1,2,3,4,5]:
    processes.append((None,i))
    pass
processes.reverse()
tx_sizes = [pow(2,13)]
page_sizes = [13]
table_view = [
    [{"sTitle":"Platform"},{"content":"object.platform()"}],
    [{"sTitle":"Config"},{"content":"'{0}'.format(object.config())"}],
    [{"sTitle":"Processes"},{"content":"object.processes()"}],
    [{"sTitle":"Rate (v/s)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}],
    [{"sTitle":"Version"},{"content":"object.engine()"}]
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","object.processes()"),"xaxis":"processes"},
        {"name":"time","data":("object.time_avg()*0.001","object.processes()"),"xaxis":"processes"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        {"name":"Config","id":"object.config_id()","content":"object.config()"},
        {"name":"Version","id":"object.engine_id()","content":"object.engine()"},
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
            "config":["local_disks:1","local_disks:2","local_disks:3","local_disks:4"],
            "page_size":page_sizes,
            "threads":threads,
            "process":processes,            
            "use_index":[1],
            "new":1,
            "size":[graph_size],
            "txsize":tx_sizes,
            "ig_version":["ig.3.1.task"],
            },
        "table_view":table_view,
        "plot_view":plot_view
        }
    ]



    


    




    
