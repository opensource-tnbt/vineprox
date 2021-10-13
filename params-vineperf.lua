function convertIPToHex(ip)
  local address_chunks = {}
  if type(ip) ~= "string" then
    print ("IP ADDRESS ERROR: ", ip)
    return "IP ADDRESS ERROR"
  end

  local chunks = {ip:match("^(%d+)%.(%d+)%.(%d+)%.(%d+)(\/%d+)$")}
  if #chunks == 5 then
    for i,v in ipairs(chunks) do
      if i < 5 then
        if tonumber(v) > 255 then
          print ("IPV4 ADDRESS ERROR: ", ip)
          return "IPV4 ADDRESS ERROR"
        end
        address_chunks[#address_chunks + 1] = string.format ("%02x", v)
      end
    end
    result = table.concat(address_chunks, " ")
    print ("Hex IPV4: ", result)
    return result
  end

  local chunks = {ip:match("^(%d+)%.(%d+)%.(%d+)%.(%d+)$")}
  if #chunks == 4 then
    for i,v in ipairs(chunks) do
      if tonumber(v) > 255 then
        print ("IPV4 ADDRESS ERROR: ", ip)
        return "IPV4 ADDRESS ERROR"
      end
      address_chunks[#address_chunks + 1] = string.format ("%02x", v)
    end
    result = table.concat(address_chunks, " ")
    print ("Hex IPV4: ", result)
    return result
  end

  delimiter = ":"
  for match in (ip..delimiter):gmatch("(.-)"..delimiter) do
    if match ~= "" then
      number = tonumber(match, 16)
      if number <= 65535 then
        table.insert(address_chunks, string.format("%02x %02x",number/256,number % 256))
      end
    else
      table.insert(address_chunks, "")
    end
  end
  for i, chunk in ipairs(address_chunks) do
    if chunk =="" then
      table.remove(address_chunks, i)
      for j = 1,(8-#address_chunks) do
        table.insert(address_chunks, i, "00 00")
      end
      break
    end
  end
  result = table.concat(address_chunks, " ")
  print ("Hex IPV6: ", result)
  return result
end

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
gencores="11,12,13"
latcores="14"
bucket_size_exp="20"
heartbeat="60"