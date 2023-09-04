# TOPOLOGY

In a flow-based model, the network device streams the traffic information,
called flow, to the management station. The format can be the Cisco proprietary
NetFlow (version 5 or version 9), the industry-standard IPFIX, or the open source
sFlow format.

Not all monitoring comes in the form of time series data.

+ We can use tools,
such as Graphviz, with a Python wrapper, to illustrate the topology.

# isntall graphviz

sudo apt-get install graphviz

devnet@PC1 ~/devnet/DEVNET/monitoring $ dot -V
dot - graphviz version 2.43.0 (0)

(venv) devnet@PC1 ~/devnet/monitoring $ pip install graphviz

(venv) devnet@PC1 ~/devnet/monitoring $ python
Python 3.11.4 (main, Jun  7 2023, 10:13:09) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import graphviz
>>> graphviz.__version__
'0.20.1'
>>> exit()

format: gv00.gv

graph my_network {
core -- distribution;
distribution -- access1;
distribution -- access2;
}

(venv) devnet@PC1 ~/devnet/DEVNET/monitoring $ dot -Tpng gv_00.gv -o output/gv_00.png

