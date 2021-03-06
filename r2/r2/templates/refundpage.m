## The contents of this file are subject to the Common Public Attribution
## License Version 1.0. (the "License"); you may not use this file except in
## compliance with the License. You may obtain a copy of the License at
## http://code.reddit.com/LICENSE. The License is based on the Mozilla Public
## License Version 1.1, but Sections 14 and 15 have been added to cover use of
## software over a computer network and provide for limited attribution for the
## Original Developer. In addition, Exhibit A has been modified to be
## consistent with Exhibit B.
##
## Software distributed under the License is distributed on an "AS IS" basis,
## WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
## the specific language governing rights and limitations under the License.
##
## The Original Code is reddit.
##
## The Original Developer is the Initial Developer.  The Initial Developer of
## the Original Code is reddit Inc.
##
## All portions of the code written by reddit are Copyright (c) 2006-2015
## reddit Inc. All Rights Reserved.
###############################################################################

<%!
  import simplejson
  from babel.numbers import format_currency, format_number
  from r2.lib.utils import to36
%>

<%namespace file="utils.m" import="plain_link"/>

<div class="refund-promotion">
  <h1>${_("refund promotion")}</h1>

  ${thing.listing}

  <h1>${_("campaign")}</h1>

  <div id="refund-form" class="pretty-form">
    <table class="content preftable">
      <tr>
        <th>${_("id")}</th>
        <td class="prefright">${thing.campaign._id36}</td>
      </tr>
      <tr>
        <th>${_("dates")}</th>
        <td class="prefright">
          ${thing.campaign.start_date.strftime("%m/%d/%Y")}
          -
          ${thing.campaign.end_date.strftime("%m/%d/%Y")}
        </td>
      </tr>
      <tr>
        <th>${_("target")}</th>
        <td class="prefright">${thing.campaign.target.pretty_name}</td>
      </tr>
      <tr>
        <th>${_("budget")}</th>
        <td class="prefright">${thing.printable_total_budget}</td>
      </tr>
      <tr>
        <th>${_("cpm")}</th>
        <td class="prefright">${thing.printable_bid}</td>
      </tr>
      <tr>
        <th>${_("impressions purchased")}</th>
        <td class="prefright">${format_number(thing.campaign.impressions, locale=c.locale)}</td>
      </tr>
      <tr>
        <th>${_("impressions received")}</th>
        <td class="prefright">
          ${format_number(thing.billable_impressions, locale=c.locale)}
          &#32;
          (${plain_link(_("detail"), thing.traffic_url)})
        </td>
      </tr>
      <tr>
        <th>${_("billable amount")}</th>
        <td class="prefright">${format_currency(thing.billable_amount, 'USD', locale=c.locale)}</td>
      </tr>
      <tr>
        <th>${_("refund amount")}</th>
        <td class="prefright">${format_currency(thing.refund_amount, 'USD', locale=c.locale)}</td>
      </tr>
    </table>

    <input type="hidden" name="link" value="${to36(thing.link._id)}"/>
    <input type="hidden" name="campaign" value="${to36(thing.campaign._id)}"/>

    <button name="save" class="btn" type="button"
            onclick="return post_pseudo_form('#refund-form', 'refund_campaign')">
      ${_("issue refund")}
    </button>
    <span class="status"></span>
  </div>

</div>