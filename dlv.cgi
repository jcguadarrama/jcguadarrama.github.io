#! /bin/bash
#############################################################################
# dlv.cgi
#
#
# Juan C. Acosta Guadarrama                                        2004--2016
#############################################################################


echo "Content-type: text/html"; echo

 # pwd

PATH="$PATH:/home/project-web/logic-lab/cgi-bin"


echo "test.cgi:"
# touch /tmp/vars 2>&1
test.cgi #> /tmp/vars$$  2>&1


echo "here1<br />"
echo "vars: <br />"
ls -la /tmp/vars$$
cat /tmp/vars$$

 echo "here4"

. /tmp/vars$$
rm /tmp/vars$$


cat << EOF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN">
<HTML>
<HEAD>
   <TITLE>DLV: $P0page</TITLE>
   <META NAME="Author" CONTENT="J.C. Acosta Guadarrama">
   <META NAME="GENERATOR" CONTENT="Mozilla/3.01Gold (X11; I; SCO_SV 3.2 i386) [Netscape]">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"></HEAD>
<body bgcolor="#FFFFFF" text="#333333" link="#006666" vlink="#666666" alink="#FF0000">
<BODY>

<p align="right"><font size="-2"><a href="../">main</a> | <a href="http://www.jguadarrama.link">research</a> | <a href="http://dblp.dagstuhl.de/pers/hd/g/Guadarrama:Juan_Carlos_Acosta">publications</a> | miscellaneous</a>

<FORM ACTION="dlv.cgi" METHOD="GET" target="_parent">
  <TABLE WIDTH="100%" CELLPADDING=0 CELLSPACING=0 >
    <TR> 
      <TD> <DIV ALIGN=right> 
          <P>
            <INPUT TYPE="RADIO" checked NAME="mode" VALUE="page">
            &#8719;:</P>
        </DIV></TD>
      <TD><textarea name="P0page" cols="50" rows="20" wrap="PHYSICAL" id="P0page" width="73">
EOF

# Fill in page
case $mode in
"page")
# echo -n "$P0page"
cat << EOF
$P0page
</textarea>
      </TD>
      <TD><div align="right"><a href="../dlv-sw.txt">switches</a>:</div></TD>
      <TD><textarea name="Epage" cols="20" rows="10" id="Epage" width="73">$Epage</textarea></TD>
    </TR>
    <TR> 
      <TD> <DIV ALIGN=right> 
          <P> 
            <INPUT TYPE="RADIO" NAME="mode" VALUE="file">
            &#8719;:</P>
        </DIV></TD>
      <TD><input name="P0file" type="file" id="P0file"></TD>
      <TD><div align="right"></div></TD>
      <TD>&nbsp;</TD>
    </TR>
  </TABLE>

<DIV ALIGN=right>
<P align="left">
      <INPUT TYPE="SUBMIT" VALUE="Answer sets">
    </P>
  </DIV>

  <CENTER>
    <P>
<HR WIDTH="95%"></P>
  </CENTER>
</FORM>
<font size="-1">
EOF


# prints answer set(s)
echo "<strong>"
# echo "$P0page" | dlv2012.bin $Epage  -- 2>&1 | awk '{print $0 "</P>"}'
cat << EOF | dlv2012.bin $Epage  -- 2>&1 | awk '{print $0 "</P>"}'
$P0page
EOF
echo "</strong><pre>"

# prints original program
echo "&#8719;: {"
echo "$P0page"; echo "}"


echo "</pre>"; echo '<HR WIDTH="95%"></P>'
;;



"file")
echo $P0file; echo
cat $P0file | dlv2012.bin $Epage  -- 2>&1
;;

esac



cat << EOF
<p>
<em><font color="#000000" size="-1"><a href="../">(AFL) J.C. Acosta-Guadarrama 2005--2016<br>
DLV is a Copyright of DLVSYSTEM s.r.l</a>
</font></em>
EOF

#echo "<pre>"
#echo "--------- translated program: ------------"
#echo "$P0page" | awk -f od2wconstr.awk
#echo "</pre>"


cat << EOF
</BODY>
</HTML>

EOF

