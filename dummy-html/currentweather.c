const char* currentweather_xml =
"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"
"<?xml-stylesheet href=\"current.xsl\" type=\"text/xsl\" ?>\n"
"<rss version=\"2.0\">\n"
"  <channel>\n"
"    <title>Current Weather</title>\n"
"    <link>\n"
"    http://www.weather.gov.hk/wxinfo/currwx/current.htm</link>\n"
"    <description>Current Weather</description>\n"
"    <language>en-us</language>\n"
"    <copyright>The content available in this file, including but\n"
"      not limited to all text, graphics, drawings, diagrams,\n"
"      photographs and compilation of data or other materials are\n"
"      protected by copyright. The Government of the Hong Kong Special\n"
"      Administrative Region is the owner of all copyright works\n"
"      contained in this website.</copyright>\n"
"    <image>\n"
"      <title>Current Weather</title>\n"
"      <link>http://www.weather.gov.hk/wxinfo/currwx/current.htm</link>\n"
"      <url>http://rss.weather.gov.hk/img/HKOlogo.gif</url>\n"
"      <width>144</width>\n"
"      <height>28</height>\n"
"    </image>\n"
"    <item>\n"
"      <author>hkowm@hko.gov.hk</author>\n"
"      <guid isPermaLink=\"false\">\n"
"        http://rss.weather.gov.hk/rss/CurrentWeather/20190704190200</guid>\n"
"      <pubDate>Thu, 04 Jul 2019 11:02:00 GMT</pubDate>\n"
"      <title>Bulletin updated at 19:02 HKT 04/07/2019</title>\n"
"      <category>R</category>\n"
"      <link>\n"
"      http://www.weather.gov.hk/wxinfo/currwx/current.htm</link>\n"
"      <description>\n"
"        <![CDATA[\n"
"         <img src=\"http://rss.weather.gov.hk/img/pic60.png\" style=\"vertical-align: middle;\">        <p>At\n"
"        7 p.m.\n"
"               at the Hong Kong Observatory :<br/>\n"
"        Air temperature : 29 degrees Celsius<br/>\n"
"        Relative Humidity : 82 per cent<br/>\n"
"		 										    																											<p></p>\n"
"                The air temperatures at other places were:\n"
"                <br/>\n"
"                <font size=\"-1\">\n"
"    <table border=\"0\" cellspacing=\"0\" cellpadding=\"0\">\n"
"    <tr><td><font size=\"-1\">Hong Kong Observatory</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">29 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">King's Park</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">28 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Wong Chuk Hang</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">29 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Ta Kwu Ling</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">28 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Lau Fau Shan</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">28 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Tai Po</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">28 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Sha Tin</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">29 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Tuen Mun</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">29 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Tseung Kwan O</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">28 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Sai Kung</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">30 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Chek Lap Kok</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">30 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Tsing Yi</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">28 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Shek Kong</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">29 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Tsuen Wan Ho Koon</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">27 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Tsuen Wan Shing Mun Valley</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">28 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Hong Kong Park</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">29 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Shau Kei Wan</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">29 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Kowloon City</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">28 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Happy Valley</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">29 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Wong Tai Sin</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">29 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Stanley</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">29 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Kwun Tong</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">29 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Sham Shui Po</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">28 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Kai Tak Runway Park</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">29 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Yuen Long Park</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">29 degrees ;</font></td></tr>\n"
"    <tr><td><font size=\"-1\">Tai Mei Tuk</font></td><td width=\"100\" align=\"right\"><font size=\"-1\">27 degrees .</font></td></tr>\n"
"    </table></font></p>\n"
"Between 5:45 and 6:45 p.m., the rainfall recorded in various regions were:<br/><br/>    <table border=\"0\" cellspacing=\"0\" cellpadding=\"0\">\n"
"                <tr><td>Yau Tsim Mong</td><td width=\"100\" align=\"right\">0 to 2&nbsp;mm;</td></tr>\n"
"            <tr><td>Central & Western District</td><td width=\"100\" align=\"right\">0 to 1&nbsp;mm;</td></tr>\n"
"            <tr><td>Kowloon City</td><td width=\"100\" align=\"right\">0 to 1&nbsp;mm;</td></tr>\n"
"            <tr><td>Kwai Tsing</td><td width=\"100\" align=\"right\">0 to 1&nbsp;mm;</td></tr>\n"
"            <tr><td>North District</td><td width=\"100\" align=\"right\">0 to 1&nbsp;mm;</td></tr>\n"
"            <tr><td>Sha Tin</td><td width=\"100\" align=\"right\">0 to 1&nbsp;mm;</td></tr>\n"
"            <tr><td>Sham Shui Po</td><td width=\"100\" align=\"right\">0 to 1&nbsp;mm;</td></tr>\n"
"            <tr><td>Tai Po</td><td width=\"100\" align=\"right\">0 to 1&nbsp;mm;</td></tr>\n"
"            <tr><td>Tsuen Wan</td><td width=\"100\" align=\"right\">0 to 1&nbsp;mm.</td></tr>\n"
"        </table><br/>\n"
"        ]]>\n"
"      </description>\n"
"    </item>\n"
"  </channel>\n"
"</rss>\n";
