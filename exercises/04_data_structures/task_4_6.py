# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.split()
Temp_Protocol = '''   
{:<25}{}
{:<25}{}
{:<25}{}
{:<25}{} 
{:<25}{}
{:<25}{}
'''
print(Temp_Protocol.format('Protocol:','OSPF',
 'Prefix:', ospf_route[1],
 'AD/Metric:', ospf_route[2][1:-1],
 'Next-Hop:', ospf_route[4][:-1],
 'Last update:', ospf_route[5][:-1],
 'Outbound Interface:', ospf_route[6]))

