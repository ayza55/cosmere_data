---
layout: home
title: Cosmere Network
---

### This page may contain spoilers for : Warbreaker

Initial attempts to create relationship networks between characters in Brandon Sanderson's **Cosmere** series.
Updated: July 2026

## Projects
<html>
    <head>
        <meta charset="utf-8">
        
            <script src="lib/bindings/utils.js"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/dist/vis-network.min.css" integrity="sha512-WgxfT5LWjfszlPHXRmBWHkV2eceiWTOBvrKCNbdgDYTHrT2AeLCGbF4sZlZw3UMN3WtL0tGUoIAKsu8mllg/XA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/vis-network.min.js" integrity="sha512-LnvoEWDFrqGHlHmDD2101OrLcbsfkrzoSpvtSQtxK3RMnRV0eOkhhBN2dXHKRrUU8p2DGRTk35n4O8nWSVe1mQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
            
        
<center>
<h1></h1>
</center>

<!-- <link rel="stylesheet" href="../node_modules/vis/dist/vis.min.css" type="text/css" />
<script type="text/javascript" src="../node_modules/vis/dist/vis.js"> </script>-->
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
          crossorigin="anonymous"
        />
        <script
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
          crossorigin="anonymous"
        ></script>


        <center>
          <h1></h1>
        </center>
        <style type="text/css">

             #mynetwork {
                 width: 100%;
                 height: 600px;
                 background-color: #ffffff;
                 border: 1px solid lightgray;
                 position: relative;
                 float: left;
             }

             

             

             
        </style>
    </head>


    <body>
        <div class="card" style="width: 100%">
            
            
            <div id="mynetwork" class="card-body"></div>
        </div>

        
        

        <script type="text/javascript">

              // initialize global variables.
              var edges;
              var nodes;
              var allNodes;
              var allEdges;
              var nodeColors;
              var originalNodes;
              var network;
              var container;
              var options, data;
              var filter = {
                  item : '',
                  property : '',
                  value : []
              };

              

              

              // This method is responsible for drawing the graph, returns the drawn network
              function drawGraph() {
                  var container = document.getElementById('mynetwork');

                  

                  // parsing and collecting nodes and edges from the python
                  nodes = new vis.DataSet([{"color": "red", "id": "Returned", "label": "Returned", "shape": "dot"}, {"color": "red", "id": "Cognitive Shadow", "label": "Cognitive Shadow", "shape": "dot"}, {"color": "red", "id": "Lifeless", "label": "Lifeless", "shape": "dot"}, {"color": "red", "id": "Royal Locks", "label": "Royal Locks", "shape": "dot"}, {"color": "red", "id": "Awakener", "label": "Awakener", "shape": "dot"}, {"color": "red", "id": "Worldhopper", "label": "Worldhopper", "shape": "dot"}, {"color": "red", "id": "Consumes Investiture", "label": "Consumes Investiture", "shape": "dot"}, {"color": "red", "id": "Surgebinder", "label": "Surgebinder", "shape": "dot"}, {"color": "red", "id": "Shardbearer", "label": "Shardbearer", "shape": "dot"}, {"color": "red", "id": "Cuts through any substance", "label": "Cuts through any substance", "shape": "dot"}, {"color": "red", "id": "Five Scholars", "label": "Five Scholars", "shape": "dot"}, {"color": "red", "id": "Denth\u0027s crew", "label": "Denth\u0027s crew", "shape": "dot"}, {"color": "red", "id": "Kholinar Wall Guard", "label": "Kholinar Wall Guard", "shape": "dot"}, {"color": "#97c2fc", "id": "Allmother", "label": "Allmother", "shape": "dot"}, {"color": "#97c2fc", "id": "Arsteel", "label": "Arsteel", "shape": "dot"}, {"color": "#97c2fc", "id": "Ashu", "label": "Ashu", "shape": "dot"}, {"color": "#97c2fc", "id": "Bebid", "label": "Bebid", "shape": "dot"}, {"color": "#97c2fc", "id": "Blushweaver", "label": "Blushweaver", "shape": "dot"}, {"color": "#97c2fc", "id": "Brighthue", "label": "Brighthue", "shape": "dot"}, {"color": "#97c2fc", "id": "Brightvison", "label": "Brightvison", "shape": "dot"}, {"color": "#97c2fc", "id": "Cads", "label": "Cads", "shape": "dot"}, {"color": "#97c2fc", "id": "Calmseer", "label": "Calmseer", "shape": "dot"}, {"color": "#97c2fc", "id": "Dedelin", "label": "Dedelin", "shape": "dot"}, {"color": "#97c2fc", "id": "Denth", "label": "Denth", "shape": "dot"}, {"color": "#97c2fc", "id": "Fafen", "label": "Fafen", "shape": "dot"}, {"color": "#97c2fc", "id": "Fob", "label": "Fob", "shape": "dot"}, {"color": "#97c2fc", "id": "Fran", "label": "Fran", "shape": "dot"}, {"color": "#97c2fc", "id": "Gagaril", "label": "Gagaril", "shape": "dot"}, {"color": "#97c2fc", "id": "Gendren", "label": "Gendren", "shape": "dot"}, {"color": "#97c2fc", "id": "Giftbeacon", "label": "Giftbeacon", "shape": "dot"}, {"color": "#97c2fc", "id": "Grable", "label": "Grable", "shape": "dot"}, {"color": "#97c2fc", "id": "Halan", "label": "Halan", "shape": "dot"}, {"color": "#97c2fc", "id": "Havarseth", "label": "Havarseth", "shape": "dot"}, {"color": "#97c2fc", "id": "Hopefinder", "label": "Hopefinder", "shape": "dot"}, {"color": "#97c2fc", "id": "Inhanna", "label": "Inhanna", "shape": "dot"}, {"color": "#97c2fc", "id": "Jewels", "label": "Jewels", "shape": "dot"}, {"color": "#97c2fc", "id": "Jlan", "label": "Jlan", "shape": "dot"}, {"color": "#97c2fc", "id": "Kindwinds", "label": "Kindwinds", "shape": "dot"}, {"color": "#97c2fc", "id": "Lemex", "label": "Lemex", "shape": "dot"}, {"color": "#97c2fc", "id": "Lemex\u0027s nurse", "label": "Lemex\u0027s nurse", "shape": "dot"}, {"color": "#97c2fc", "id": "Lifeblesser", "label": "Lifeblesser", "shape": "dot"}, {"color": "#97c2fc", "id": "Llarimar", "label": "Llarimar", "shape": "dot"}, {"color": "#97c2fc", "id": "Lolan", "label": "Lolan", "shape": "dot"}, {"color": "#97c2fc", "id": "Mab", "label": "Mab", "shape": "dot"}, {"color": "#97c2fc", "id": "Mercystar", "label": "Mercystar", "shape": "dot"}, {"color": "#97c2fc", "id": "Mirthgiver", "label": "Mirthgiver", "shape": "dot"}, {"color": "#97c2fc", "id": "Misel", "label": "Misel", "shape": "dot"}, {"color": "#97c2fc", "id": "Nanrovah", "label": "Nanrovah", "shape": "dot"}, {"color": "#97c2fc", "id": "Nenefra", "label": "Nenefra", "shape": "dot"}, {"color": "#97c2fc", "id": "Nightblood", "label": "Nightblood", "shape": "dot"}, {"color": "#97c2fc", "id": "Old Chapps", "label": "Old Chapps", "shape": "dot"}, {"color": "#97c2fc", "id": "Parlin", "label": "Parlin", "shape": "dot"}, {"color": "#97c2fc", "id": "Paxen", "label": "Paxen", "shape": "dot"}, {"color": "#97c2fc", "id": "Peaceyearning", "label": "Peaceyearning", "shape": "dot"}, {"color": "#97c2fc", "id": "Rariv", "label": "Rariv", "shape": "dot"}, {"color": "#97c2fc", "id": "Ridger", "label": "Ridger", "shape": "dot"}, {"color": "#97c2fc", "id": "Rira (character)", "label": "Rira (character)", "shape": "dot"}, {"color": "#97c2fc", "id": "Shashara", "label": "Shashara", "shape": "dot"}, {"color": "#97c2fc", "id": "Sisirinah", "label": "Sisirinah", "shape": "dot"}, {"color": "#97c2fc", "id": "Lightsong", "label": "Lightsong", "shape": "dot"}, {"color": "#97c2fc", "id": "Stillmark", "label": "Stillmark", "shape": "dot"}, {"color": "#97c2fc", "id": "Susebron", "label": "Susebron", "shape": "dot"}, {"color": "#97c2fc", "id": "Susebron the Fourth", "label": "Susebron the Fourth", "shape": "dot"}, {"color": "#97c2fc", "id": "Susebron\u0027s mother", "label": "Susebron\u0027s mother", "shape": "dot"}, {"color": "#97c2fc", "id": "Taff", "label": "Taff", "shape": "dot"}, {"color": "#97c2fc", "id": "Tatara", "label": "Tatara", "shape": "dot"}, {"color": "#97c2fc", "id": "Thame", "label": "Thame", "shape": "dot"}, {"color": "#97c2fc", "id": "Tonk Fah", "label": "Tonk Fah", "shape": "dot"}, {"color": "#97c2fc", "id": "Treledees", "label": "Treledees", "shape": "dot"}, {"color": "#97c2fc", "id": "Truthcall", "label": "Truthcall", "shape": "dot"}, {"color": "#97c2fc", "id": "Tuft", "label": "Tuft", "shape": "dot"}, {"color": "#97c2fc", "id": "Vahr", "label": "Vahr", "shape": "dot"}, {"color": "#97c2fc", "id": "Vasher", "label": "Vasher", "shape": "dot"}, {"color": "#97c2fc", "id": "Vivenna", "label": "Vivenna", "shape": "dot"}, {"color": "#97c2fc", "id": "Vivenna\u0027s Blade", "label": "Vivenna\u0027s Blade", "shape": "dot"}, {"color": "#97c2fc", "id": "Vivenna\u0027s mother", "label": "Vivenna\u0027s mother", "shape": "dot"}, {"color": "#97c2fc", "id": "Vo", "label": "Vo", "shape": "dot"}, {"color": "#97c2fc", "id": "Weatherlove", "label": "Weatherlove", "shape": "dot"}, {"color": "#97c2fc", "id": "Yarda", "label": "Yarda", "shape": "dot"}, {"color": "#97c2fc", "id": "Yesteel", "label": "Yesteel", "shape": "dot"}]);
                  edges = new vis.DataSet([{"from": "Returned", "to": "Allmother"}, {"from": "Cognitive Shadow", "to": "Allmother"}, {"from": "Returned", "to": "Arsteel"}, {"from": "Lifeless", "to": "Arsteel"}, {"from": "Cognitive Shadow", "to": "Arsteel"}, {"from": "Five Scholars", "to": "Arsteel"}, {"from": "Denth\u0027s crew", "to": "Arsteel"}, {"from": "Returned", "to": "Blushweaver"}, {"from": "Cognitive Shadow", "to": "Blushweaver"}, {"from": "Returned", "to": "Brighthue"}, {"from": "Cognitive Shadow", "to": "Brighthue"}, {"from": "Returned", "to": "Brightvison"}, {"from": "Cognitive Shadow", "to": "Brightvison"}, {"from": "Returned", "to": "Calmseer"}, {"from": "Cognitive Shadow", "to": "Calmseer"}, {"from": "Royal Locks", "to": "Dedelin"}, {"from": "Returned", "to": "Denth"}, {"from": "Awakener", "to": "Denth"}, {"from": "Worldhopper", "to": "Denth"}, {"from": "Cognitive Shadow", "to": "Denth"}, {"from": "Royal Locks", "to": "Denth"}, {"from": "Five Scholars", "to": "Denth"}, {"from": "Denth\u0027s crew", "to": "Denth"}, {"from": "Royal Locks", "to": "Fafen"}, {"from": "Returned", "to": "Giftbeacon"}, {"from": "Cognitive Shadow", "to": "Giftbeacon"}, {"from": "Returned", "to": "Hopefinder"}, {"from": "Cognitive Shadow", "to": "Hopefinder"}, {"from": "Denth\u0027s crew", "to": "Jewels"}, {"from": "Returned", "to": "Kindwinds"}, {"from": "Cognitive Shadow", "to": "Kindwinds"}, {"from": "Awakener", "to": "Lemex"}, {"from": "Worldhopper", "to": "Lemex\u0027s nurse"}, {"from": "Returned", "to": "Lifeblesser"}, {"from": "Cognitive Shadow", "to": "Lifeblesser"}, {"from": "Returned", "to": "Mercystar"}, {"from": "Cognitive Shadow", "to": "Mercystar"}, {"from": "Returned", "to": "Mirthgiver"}, {"from": "Cognitive Shadow", "to": "Mirthgiver"}, {"from": "Consumes Investiture", "to": "Nightblood"}, {"from": "Surgebinder", "to": "Nightblood"}, {"from": "Worldhopper", "to": "Nightblood"}, {"from": "Returned", "to": "Peaceyearning"}, {"from": "Cognitive Shadow", "to": "Peaceyearning"}, {"from": "Royal Locks", "to": "Ridger"}, {"from": "Returned", "to": "Shashara"}, {"from": "Awakener", "to": "Shashara"}, {"from": "Worldhopper", "to": "Shashara"}, {"from": "Cognitive Shadow", "to": "Shashara"}, {"from": "Shardbearer", "to": "Shashara"}, {"from": "Royal Locks", "to": "Shashara"}, {"from": "Five Scholars", "to": "Shashara"}, {"from": "Royal Locks", "to": "Sisirinah"}, {"from": "Returned", "to": "Lightsong"}, {"from": "Cognitive Shadow", "to": "Lightsong"}, {"from": "Returned", "to": "Stillmark"}, {"from": "Cognitive Shadow", "to": "Stillmark"}, {"from": "Returned", "to": "Susebron"}, {"from": "Awakener", "to": "Susebron"}, {"from": "Cognitive Shadow", "to": "Susebron"}, {"from": "Returned", "to": "Susebron the Fourth"}, {"from": "Awakener", "to": "Susebron the Fourth"}, {"from": "Cognitive Shadow", "to": "Susebron the Fourth"}, {"from": "Denth\u0027s crew", "to": "Tonk Fah"}, {"from": "Returned", "to": "Truthcall"}, {"from": "Cognitive Shadow", "to": "Truthcall"}, {"from": "Awakener", "to": "Vahr"}, {"from": "Returned", "to": "Vasher"}, {"from": "Awakener", "to": "Vasher"}, {"from": "Worldhopper", "to": "Vasher"}, {"from": "Cognitive Shadow", "to": "Vasher"}, {"from": "Shardbearer", "to": "Vasher"}, {"from": "Five Scholars", "to": "Vasher"}, {"from": "Royal Locks", "to": "Vivenna"}, {"from": "Awakener", "to": "Vivenna"}, {"from": "Worldhopper", "to": "Vivenna"}, {"from": "Shardbearer", "to": "Vivenna"}, {"from": "Kholinar Wall Guard", "to": "Vivenna"}, {"from": "Cuts through any substance", "to": "Vivenna\u0027s Blade"}, {"from": "Returned", "to": "Vo"}, {"from": "Cognitive Shadow", "to": "Vo"}, {"from": "Returned", "to": "Weatherlove"}, {"from": "Cognitive Shadow", "to": "Weatherlove"}, {"from": "Returned", "to": "Yesteel"}, {"from": "Awakener", "to": "Yesteel"}, {"from": "Five Scholars", "to": "Yesteel"}]);

                  nodeColors = {};
                  allNodes = nodes.get({ returnType: "Object" });
                  for (nodeId in allNodes) {
                    nodeColors[nodeId] = allNodes[nodeId].color;
                  }
                  allEdges = edges.get({ returnType: "Object" });
                  // adding nodes and edges to the graph
                  data = {nodes: nodes, edges: edges};

                  var options = {
    "configure": {
        "enabled": false
    },
    "edges": {
        "color": {
            "inherit": true
        },
        "smooth": {
            "enabled": true,
            "type": "dynamic"
        }
    },
    "interaction": {
        "dragNodes": true,
        "hideEdgesOnDrag": false,
        "hideNodesOnDrag": false
    },
    "physics": {
        "enabled": true,
        "stabilization": {
            "enabled": true,
            "fit": true,
            "iterations": 1000,
            "onlyDynamicEdges": false,
            "updateInterval": 50
        }
    }
};

                  


                  

                  network = new vis.Network(container, data, options);

                  

                  

                  


                  

                  return network;

              }
              drawGraph();
        </script>
    </body>
</html>