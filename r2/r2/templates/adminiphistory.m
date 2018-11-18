<%!
  from r2.lib.template_helpers import display_link_karma
%>
<%namespace file="utils.m" import="timestamp, thing_timestamp, plain_link" />
<h1>IP History for&nbsp;${plain_link(thing.user.name, "/user/%s/" % thing.user.name, _sr_path=False)}</h1>
<br/>
<table class="lined-table">
 <thead>
   <tr>
    <th>IP</th>
    <th>Source</th>
    <th>Ago</th>
    <th>Date</th>
  </tr>
 </thead>
 <tbody>
  %for item in thing.iphistory:
   <tr>
     <td>${item['ip']}&nbsp;<a target="_blank" href="https://tools.keycdn.com/geo?host=${item['ip']}">[1]</a>&nbsp;<a target="_blank" href="https://fullip.info/service/lookup/${item['ip']}">[2]</a></td>
     <td>${item['type']}</td>
     <td>${timestamp(item['date'])}</td>
     <td>${item['date'].strftime("%Y-%m-%dT%H:%M:%S")}</td>
   </tr>
  %endfor
 </tbody>
</table>
