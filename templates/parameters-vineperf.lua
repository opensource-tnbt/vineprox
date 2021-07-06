require "helper"
eal="--socket-mem=256,0 --file-prefix Generator -w 0000:81:00.0 -w 0000:81:00.1"
name="Generator"
local_ip1="192.168.30.11/24"
local_hex_ip1=convertIPToHex(local_ip1)
local_ip2="192.168.30.12/24"
local_hex_ip2=convertIPToHex(local_ip2)
mcore="10"
dest_ip1="192.168.30.12/24"
dest_hex_ip1=convertIPToHex(dest_ip1)
dest_hex_mac2="de ad c3 52 79 9a"
dest_ip2="192.168.30.11/24"
dest_hex_ip2=convertIPToHex(dest_ip2)
dest_hex_mac1="de ad c3 52 79 9b"
gencores="11-13"
latcores="14-16"
bucket_size_exp="11"
heartbeat="60"