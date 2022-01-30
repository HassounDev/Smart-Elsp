var nodeIds, shadowState, nodesArray, nodes, edgesArray, edges, network;

var popoverContent = function(volumeDepart,volumeDown,volumeUp,volumeArrive, weightDepart,weightDown,weightUp,weightArrive,cls="info" ){
  var content = '<div class="panel panel-'+cls+'">'+
                          '<div class="panel-heading">'+
                            '<i class="fa fa-truck"></i> Véhicule : Truck XA1'+
                          '</div>'+
                          '<div class="panel-body">'+
                            '<table class="table table-bordered">'+
                              '<tr>'+
                                '<td class="'+cls+'">#</td>'+
                                '<td class="'+cls+'"><i class="fa fa-chevron-circle-down"></i></td>'+
                                '<td class="'+cls+'"><i class="fa fa-long-arrow-down"></i></td>'+
                                '<td class="'+cls+'"><i class="fa fa-long-arrow-up"></i></td>'+
                                '<td class="'+cls+'"><i class="fa fa-chevron-circle-up"></i></td>'+
                              '</trx>'+
                              '<tr>'+
                                '<td class="'+cls+'">LU</td>'+
                                '<td class="'+cls+'">...</td>'+
                                '<td class="'+cls+'">...</td>'+
                                '<td class="'+cls+'">...</td>'+
                                '<td class="'+cls+'">...</td>'+
                              '</tr>'+
                              '<tr>'+
                                '<td class="'+cls+'">V (m³)</td>'+
                                '<td class="'+cls+'">'+ volumeDepart +'</td>'+
                                '<td class="'+cls+'">'+ volumeDown + '</td>'+
                                '<td class="'+cls+'">'+ volumeUp + '</td>'+
                                '<td class="'+cls+'">'+ volumeArrive + '</td>'+
                              '</tr>'+
                              '<tr>'+
                                '<td class="'+cls+'">P <small>(kg)</small></td>'+
                                '<td class="'+cls+'">'+ weightDepart +'</td>'+
                                '<td class="'+cls+'">'+ weightDown +'</td>'+
                                '<td class="'+cls+'">'+ weightUp +'</td>'+
                                '<td class="'+cls+'">'+ weightArrive +'</td>'+
                              '</tr>'+
                            '</table>'+
                          '</div>'+
                        '</div>';
                        return content;
}

    function startNetwork() {
        // this list is kept to remove a random node.. we do not add node 1 here because it's used for changes
        shadowState = false;


        // create an array with nodes
        nodesArray = [
          {id: 1, x:403, y:444, physics:false, label: 'Centre Commercial Mabrouk' ,shape: 'dot'},
          {id: 2, x:842, y:385, physics:false, label: 'Kasbah Museum' ,shape: 'dot'},
          {id: 3, x:572, y:339, physics:false, label: 'Merchan' ,shape: 'dot'},
          {id: 4, x:857, y:177, physics:false, label: 'Malabata ' ,shape: 'dot'},
          {id: 5, x:675, y:199, physics:false, label: 'Aéroport de Tanger – Ibn Battouta' ,shape: 'dot'},
          {id: 6, x:537, y:57, physics:false, label: 'Casabarata' ,shape: 'dot'},
          {id: 7, x:474, y:210, physics:false, label: 'Kaissariat Al Azhar' ,shape: 'dot'},
          {id: 8, x:254, y:296, physics:false, label: 'Pharmacie Beni Makada' ,shape: 'dot'},
          {id: 9, x:163, y:439, physics:false, label: 'Ain Hayani' ,shape: 'dot'},
          {id: 10, x:236, y:143, physics:false, label: 'Mesallah' ,shape: 'dot'},
          {id: 11, x:61, y:125, physics:false, label: 'Rmilat' ,shape: 'dot'},
          {id: 12, x:356, y:61, physics:false, label: 'Boubana' ,shape: 'dot'}
        ];
        nodes = new vis.DataSet(nodesArray);

        // create an array with edges
        edgesArray = [
          {id:12, from: 1, to: 2},
          {id:13, from: 1, to: 3},
          {id:23, from: 2, to: 3},
          {id:24, from: 2, to: 4},
          {id:25, from: 2, to: 5},
          {id:35, from: 3, to: 5},
          {id:45, from: 4, to: 5},
          {id:46, from: 4, to: 6},
          {id:57, from: 5, to: 7},
          {id:59, from: 5, to: 9},
          {id:67, from: 6, to: 7},
          {id:68, from: 6, to: 8},
          {id:612, from: 6, to: 12},
          {id:87, from: 8, to: 7},
          {id:89, from: 8, to: 9},
          {id:811, from: 8, to: 11},
          {id:810, from: 8, to: 10},
          {id:911, from: 9, to: 11},
          {id:1011, from: 10, to: 11},
          {id:1012, from: 10, to: 12},
          {id:1211, from: 12, to: 11},



        ];
        edges = new vis.DataSet(edgesArray);

        // create a network
        var container = document.getElementById('mynetwork');
        var data = {
            nodes: nodes,
            edges: edges
        };
        var options = {
          autoResize: true,
          nodes: {
          borderWidth:4,
          size:25,
	      color: {
            border: '#222222',
            background: '#666666'
          },
          font:{color:'#eeeeee'}
        },
        edges: {
          color: 'lightgray',
          width: 2
        }
        };
        network = new vis.Network(container, data, options);

        /*network.on("dragging", function (params) {
            params.event = "[original event]";
            document.getElementById('eventSpan').innerHTML = '<h2>dragging event:</h2>' + JSON.stringify(params, null, 4);
        });*/
    }



    function drawPath() {
    var edgeColor = "#86f23a";
    var nodeColor = "#42f445";
    var endColor = "#cc0619";
    var middleColor = "#f4f400";

    nodes.update([
      {id:1, color:{background:nodeColor}},
      {id:2, color:{background:nodeColor}},
      {id:4, color:{background:nodeColor}},
      {id:6, color:{background:nodeColor}},
      {id:7, color:{background:nodeColor}},
      {id:12, color:{background:nodeColor}}
    ]);
    edges.update([{id:12, color:{color:edgeColor}},{id:24, color:{color:edgeColor}},{id:46, color:{color:edgeColor}},{id:612, color:{color:edgeColor}},{id:67,color:{color:edgeColor}}]);


    setTimeout(function(){
      nodes.update([{id:1, color:{background:endColor},title: popoverContent(0,0,14,14,0,0,14000,14000)}]);
      edges.update([{id:12, color:{color:endColor}}]);
      network.animateTraffic([
          {edge:12, trafficSize:8},
      ]);
    },1000)

    setTimeout(function(){

      nodes.update([{id:2, color:{background:endColor}, title: popoverContent(14,1,13,13,14000,3000,1000,12000)}]);
      edges.update([{id:24, color:{color:endColor}}]);
      network.animateTraffic([
          {edge:24, trafficSize:5},
      ]);
    },4000);
    setTimeout(function(){
      nodes.update([{id:4, color:{background:endColor}, title: popoverContent(13,2,11,20,13000,3000,2000,10000)}]);
      edges.update([{id:46, color:{color:endColor}}]);
      network.animateTraffic([
          {edge:46, trafficSize:7},
      ]);
    },6000);
    setTimeout(function(){
      nodes.update([{id:6, color:{background:middleColor}, title: popoverContent(11,2,9,10,10000,5000,4000,8000,"warning")}]);
      edges.update([{id:612, color:{color:endColor}}]);
      network.animateTraffic([
          {edge:612, trafficSize:3},
      ]);
    },8000);

    setTimeout(function(){
      nodes.update([{id:12, color:{background:endColor}, title: popoverContent(9,3,5,7,8000,4000,2000,6000)}]);
      network.animateTraffic([
          {edge:612, trafficSize:2, isBackward: true}
      ]);
    },10000);

    setTimeout(function(){
      nodes.update([{id:6, color:{background:endColor}, title: popoverContent(5,4,0,1,5000,4000,0,1000,"warning")}]);
      edges.update([{id:67, color:{color:endColor}}]);
      network.animateTraffic([
          {edge:67, trafficSize:2}
      ]);
    },12000);

    setTimeout(function(){
      nodes.update([{id:7, color:{background:endColor}, title: popoverContent(1,0,0,0,1000,1000,0,0)}]);
      /*edges.update([{id:67, color:{color:endColor}}]);
      network.animateTraffic([
          {edge:67, trafficSize:2}
      ]);*/
    },14000);

    /*setTimeout(function(){
      alert('test');
    },8000);

    ,

    {edge:612, trafficSize:1}
    */
    }

    function addNode() {
        var newId = (Math.random() * 1e7).toString(32);
        nodes.add({id:newId, label:"New Position"});
        nodeIds.push(newId);
    }

    function changeNode1() {
        var newColor = '#' + Math.floor((Math.random() * 255 * 255 * 255)).toString(16);
        nodes.update([{id:1, color:{background:newColor}}]);
    }

    function removeRandomNode() {
        var randomNodeId = nodeIds[Math.floor(Math.random() * nodeIds.length)];
        nodes.remove({id:randomNodeId});

        var index = nodeIds.indexOf(randomNodeId);
        nodeIds.splice(index,1);
    }

    function changeOptions() {
        shadowState = !shadowState;
        network.setOptions({nodes:{shadow:shadowState},edges:{shadow:shadowState}});
    }

    function resetAllNodes() {
        nodes.clear();
        edges.clear();
        nodes.add(nodesArray);
        edges.add(edgesArray);
    }

    function resetAllNodesStabilize() {
        resetAllNodes();
        network.stabilize();
    }

    function setTheData() {
        nodes = new vis.DataSet(nodesArray);
        edges = new vis.DataSet(edgesArray);
        network.setData({nodes:nodes, edges:edges})
    }

    function resetAll() {
        if (network !== null) {
            network.destroy();
            network = null;
        }
        startNetwork();
    }

    startNetwork();
