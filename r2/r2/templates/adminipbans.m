<%!
  from r2.lib.template_helpers import display_link_karma
%>
<%namespace file="utils.m" import="error_field, thing_timestamp, plain_link" />
<%namespace file="printablebuttons.m" import="ynbutton" />

<%def name="ipbannew()">
 <form action="/post/editipban"
       method="post"
       class="pretty-form medium-text"
       style="display:none"
       onsubmit="return post_form(this, 'editipban');"
       id="addipban">
  <input type="hidden" name="fullname" value="NEW" />
  <table class="off-lined-table borderless">
    <tr>
      <td><label for="ip">ip</label></td>
      <td>
          <input type="text" name="ip" id="ip" required="required" />
          ${error_field("NO_TEXT", "ip", "span")}
          ${error_field("INVALID_OPTION", "ip", "span")}
          ${error_field("USER_DOESNT_EXIST", "ip", "span")}
      </td>
    </tr>
    <tr>
      <td><label for="notes">admin note</label></td>
      <td>
        <input type="text" name="notes" id="notes" value="" />
        ${error_field("NO_TEXT", "notes", "span")}
      </td>
    </tr>
  </table>
  <button class="btn" type="submit">add</button>
  <button class="btn" onclick="$(this).closest('form').hide(); return false;">cancel</button>
  <span class="status"></span>
  <br/>
 </form>
</%def>

<%def name="ipbanedit(formid, ip='', notes='')">
 <form action="/post/editipban" method="post" class="pretty-form medium-text"
       style="display:none" onsubmit="return post_form(this, 'editipban');" id="ipbanedit-${formid}">

  <input type="hidden" name="fullname" value="${formid}" />
  <input type="hidden" name="ip" value="${ip}" />

  <input type="text" name="notes" id="notes" value="${notes}" />
        ${error_field("NO_TEXT", "notes", "span")}
  <button class="btn" type="submit">update</button>
  <span class="status"></span>
 </form>
</%def>

<h1>ip bans</h1>
<a href="#" onclick="$('#addipban').toggle(); return false;">add ban</a>
${ipbannew()}
<br/>
<br/>

<div class="usertable ip-bans">
  <table>
   <tbody>
    %for ban in thing.bans:
     <tr>
       <td>${ban.ip}&nbsp;<a target="_blank" href="https://tools.keycdn.com/geo?host=${ban.ip}">[1]</a>&nbsp;<a target="_blank" href="https://fullip.info/service/lookup/${ban.ip}">[2]</a></td>
       <td></td>
       <td>${thing_timestamp(ban)} &nbsp;ago</td>
       <td>
         ${ynbutton(op='deleteipban',
                 title=_("remove"),
                 executed=_('ip ban removed, <a href="#" onclick="location.reload();">reload</a> to see changes'),
                 hidden_data=dict(ipban_id=ban._fullname),
                 question=_("remove ip ban?"),
                 access_required=False)}
       </td>
       <td><a href="#" onclick="$('#ipbanedit-${ban._fullname}').toggle(); return false;">edit</a></td>
       <td>
         ${ban.notes}
         ${ipbanedit(ban._fullname, ban.ip, ban.notes)}
       </td>
     </tr>
    %endfor
   </tbody>
  </table>
</div>
