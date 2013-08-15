name = "dataset size (no query)"

tx_sizes = [pow(2,10)]
page_sizes = [13]
graph_sizes = []
for i in xrange(10,17):
    graph_sizes.append(pow(2,i))
    pass

description = "Ingest as a function of data size (transaction size {0}, page size {1} without performing any query).".format(tx_sizes,page_sizes)

table_view = [
    [{"sTitle":"Platform"},{"content":"object.platform()"}],
    [{"sTitle":"Dataset Size"},{"content":"object.graph_size()"}],
    [{"sTitle":"Rate (ops/sec)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}]
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","math.log(object.graph_size(),2)"),"xaxis":"pow(2,dataset size)"},
        {"name":"time","data":("object.time_avg()*0.001","math.log(object.graph_size(),2)"),"xaxis":"pow(2,dataset size)"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        ]
}

cases = []
cases.append(
    {
        "name":"standard",
        "description":"Composite Ingest as a function of dataset size (no query)",
        "type":"composite_ingest",
        "data":
        {
            "composite_name":"BaseModel.noquery",
            "template":["whois"],
            "config":["default:default"],
            "page_size":page_sizes,
            "threads":[1],
            "use_index":[1],
            "new":1,
            "size":graph_sizes,
            "txsize":tx_sizes,
            "ig_version":["ig.3.1.task"]
            },
        "table_view":table_view,
        "plot_view":plot_view
        }
    )



    


    




    
