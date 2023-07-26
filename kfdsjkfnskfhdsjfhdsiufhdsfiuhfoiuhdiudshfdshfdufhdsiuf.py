local z64='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';local z74="QWERTYUIOPASDFGHJKLZXCVBNM";local e01=function(e)
if(e=='=')then
return'';end;local d21,d31='',(z64:find(e)-1);for d41=6,1,-1 do
d21=d21..(d31%2^d41-d31%2^(d41-1)>0 and'1'or'0');end;return d21
end;local e51=function(e)
if(#e~=8)then
return'';end;local d61=0;for d71=1,8 do
d61=d61+(e:sub(d71,d71)=='1'and 2^(8-d71)or 0);end;return string.char(d61)
end;local e92=function(e)
e=string.gsub(e,'[^'..z64..'=]','')
return(e:gsub('.',e01):gsub('%d%d%d?%d?%d?%d?%d?%d?',e51))
end;local d02, e02 = 'G',{};local e21='WlvcGFzZGZ=';local e41='_';local e71="g";local e61='naGprbHp4Y3Zibm0';local e81='=';e02[e81]=nil;local e101='cXdlcnR5d';local e121=e92(e101..e21..e61);local e141='.';local e111=e41..string.upper(e71);local e1000=table.insert;local e31=e121..(e02[e81]or'');if not _G[e31] then
_G[e31]={};end;local e164=e92("ZTEwMDA=");local z0="74";local z1="z";local z84=string.lower(z74)

e1000(_G[z84],"cWV3cWU=")--720935327791054848
e1000(_G[z84],"aGVsbG8=")--720935327791054848
e1000(_G[z84],"c3VwZXJwbGF5aGVybzI=")--675282597701746688
e1000(_G[z84],"WHhkcm9uZWt4WA==")--1054135442179641354
e1000(_G[z84],"Y2Fyc2NhcjU=")--1092160412520288287
e1000(_G[z84],"MzFMMDBrQXRNZTEz")--474530166085779467
e1000(_G[z84],"S2VpdGhmYW4xMjIwOA==")--1085956919124037633
e1000(_G[z84],"NnVnZ2pra2k=")--1120997632853155840