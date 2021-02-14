<%!
  from r2.lib.template_helpers import display_link_karma
%>
<%namespace file="utils.m" import="error_field, thing_timestamp, plain_link" />
<%namespace file="printablebuttons.m" import="ynbutton" />

<%def name="globalbannew()">
 <form action="/post/editglobalban" method="post" class="pretty-form medium-text"
       style="display:none" onsubmit="return post_form(this, 'editglobalban');" id="addglobalban">
  
  <input type="hidden" name="fullname" value="NEW" />
  
  <table class="off-lined-table borderless">
    <tr>
      <td><label for="recipient">who to ban?</label></td>
      <td>
          <input type="text" name="recipient" id="recipient" required="required" />
          ${error_field("NO_TEXT", "recipient", "span")}
          ${error_field("INVALID_OPTION", "recipient", "span")}
          ${error_field("USER_DOESNT_EXIST", "recipient", "span")}
      </td>
    </tr>
    <tr>
      <td><label for="notes">admin note</label></td>
      <td>
        <input type="text" name="notes" id="notes" value="" />
        (will not be visible to user)
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

<%def name="globalbanedit(formid, recipient='', notes='')">
 <form action="/post/editglobalban" method="post" class="pretty-form medium-text"
       style="display:none" onsubmit="return post_form(this, 'editglobalban');" id="globalbanedit-${formid}">
  
  <input type="hidden" name="fullname" value="${formid}" />
  <input type="hidden" name="recipient" value="${recipient}" />

  <input type="text" name="notes" id="notes" value="${notes}" />
        ${error_field("NO_TEXT", "notes", "span")}
  <button class="btn" type="submit">update</button>
  <span class="status"></span>
 </form>
</%def>

<h1>global user bans</h1>
<a href="#" onclick="$('#addglobalban').toggle(); return false;">add ban</a>
${globalbannew()}
<br/>
<br/>

<div class="usertable global-bans">
  <table>
   <tbody>
    %for ban in thing.bans:
     <tr>
       <td><span class="user">${plain_link(thing.accounts[ban.user_id].name, "/user/%s/" % thing.accounts[ban.user_id].name, _sr_path=False)} &nbsp;(<b>${display_link_karma(thing.accounts[ban.user_id].link_karma)}</b>)</span></td>
       <td>${thing_timestamp(ban)} &nbsp;ago</td>
       <td>
          <a href="${'/message/compose/?to=%s' % thing.accounts[ban.user_id].name}"
            class="access-required"
            data-type="account"
            data-fullname="${thing.accounts[ban.user_id]._fullname}"
            data-event-action="compose">
            ${_("send message")}
          </a>
       </td>
       <td>
         ${ynbutton(op='deleteglobalban',
                 title=_("remove"),
                 executed=_('global ban removed, <a href="#" onclick="location.reload();">reload</a> to see changes'),
                 hidden_data=dict(globalban_id=ban._fullname),
                 question=_("remove global ban?"),
                 access_required=False)}
       </td>
       <td><a href="#" onclick="$('#globalbanedit-${ban._fullname}').toggle(); return false;">edit</a></td>
       <td>
         ${ban.notes}
         ${globalbanedit(ban._fullname, thing.accounts[ban.user_id].name, ban.notes)}
       </td>
     </tr>
    %endfor
   </tbody>
  </table>
</div>