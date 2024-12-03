
import re

def calculate_sum_with_conditions(text):

    mul_pattern = r"mul\((\d+),(\d+)\)"
    

    extract_enabled = True
    total_sum = 0

    tokens = re.findall(r"don't\(\)|do\(\)|mul\(\d+,\d+\)", text)

    for token in tokens:

        if token == "don't()":
            extract_enabled = False
            continue


        if token == "do()":
            extract_enabled = True
            continue

        if extract_enabled and "mul" in token:
            match = re.match(mul_pattern, token)
            if match:
                x, y = map(int, match.groups())
                total_sum += x * y

    return total_sum



text = """
*how())@*mul(666,399)?mul(354,686)<%why()}#mul(449,25)<{@mul(298,550)'why()*select()mul(39,588)-:mul(255,532)when()from()&~from()-}~!mul(501,122)what()who()/@mul(792,556) >~<when()when()!!mul(459,837)$when(){mul(390,842),who()[;mul(281,40) ']<+'}mul(19,457)@?--mul(699,994)-where()&'where()~mul(693,719)?${&;mul(561,466)why()mul(355,786) +'&'[{what()*%mul(669,354)'/how() {-who()-#mul(691,921)),'why()!don't()@who()~'<when()/mul(70,361)where()why() >'@<*$mul(389,684)/<'mul(941,352)<<from()^{ ]mul(635,25)from()select()<@what(701,307)'mul(450,613)mul(983,770)')%<&from()?>do();-:%*~mul(302,652)how()mul(827,262)>select()-#]what()who()~mul(636,791)*where()&^^'mul(267,79)'!#mul(153,490))>/!mul(429,93)where()?{where()/,mul(481,952)mul(498,420)'why()~;$how(11,770)+mul(40,723)<@do()mul(172,376)how()(%what()what()#do()who(458,15)*who()what(263,940)('mul(36,67)what()why()-do()how()/]what()mul(553,221);})what()mul(768,886)}mul(429,845)#'mul(130,55)mul(550,213)don't()+&'mul(549,688)from()-how(667,895)~>+ @[mul(242,556)~!from()-(  mul(553,356)~)}@mul(776,253)?select()how()/?#}+who()mul(132,392)$](/^%from()-/mul(153,281)what()what()mul(413,677)mul(453,733)how()mul(670,617)-!~]* select()?'#mul(140,989)~? [^mul(189,660)<mul(413,897)what()>$*>$,who()why()&mul(70,862)-^ &-*~why(),don't(){%#<+mul(830,572)$:mul(251,305)from()from()), /?;don't()}why();+from()&]when()mul(57,686)$why()!why()why()?don't()&(mul(541,775)}do();#}^?* @mul(248,215)}({select()mul(9,131)don't()-mul(222,367)?mul(541,161)({{why()@mul(613,749)don't()who()?/)&why()%%mul(970,606)*select()/)from()/}where()select()mul(623,855)//'#*:)>^mul(658,630)<mul(58,806)who()why()from()]!how()why()*mul(48,392)]who()~> mul(692,468)why():when()$mul(791,491)!%~mul(274,776)%;(]'?when(225,182)@what(28,557)[mul(33,589)+'*,+:mul(581,732)select()}?*(~,,mul(221,532)&:>mul(406,25)select()don't() !who()when()@;what()mul(399,473)>how(943,174) ):)mul(30,985),when()/* when()mul(275,577)@$?,+:('@mul(624,769)'where()&(]??$~mul(747,57)-%%/%? }*}mul(562,665)^where();why()#$:,]mul(545,73){from()why()]mul(504,381)>what()why()$%from(53,115)%mul(582where()%[select()<<mul(837,216)who()mul(483,441);what()!mul(93,242)(when(191,120)mul(252,628))why()why()[mul(703,199)#}/;[-{;%mul(463,472):why()where()>why()>who()'mul(483,928)don't()mul(303,515)<&/mul(940,761)!(/~what(585,344)where()mul(741,802)how(),~[from()%;%mul+,}]])select()mul(653,959))mul(354,159)mul(608,836)when()''who()why()select()why()}mul(167,648)mul(585,942)%who()] (~don't()mul(27,685)^}<mul(758,155)>!where()~<$,'who()mul(509,539)why(){^}from()when()who()+mul(463,984)who()$mul(579,325))?how()] who()-mul(679,71)who()^/,'[~do() )!]!mul(511,894)-+'how()~~;what()mul(845,706)#][^%^what()when()mul(968,989))[,mul(644,209)why()%;where()select()^mul(351,869)~%:]where()#mul(449,265)don't()@(^mul(569,652)why()!how()~<(mul(251,97)how()~*}#&{?;{mul(693,636)what()don't()why()how()when()who()<why()(mul(318,357)$- mul(654select()}~why()+#!why()![[mul(806,840)-$what(945,575)mul(403,681):#-mul(927,921)who()@mul(110,215)who() )mul(991,118)[#[what()^mul(517,977),,when()<mul(785,581):when()!%>when()'select(277,840)select()*don't()%+how()select()&?mul(232,345)! mul(45,51)*;,~&mul(831,663)$when()'how()do(){>!> when()mul(535,567)
who()@from(){%#where()how(){mul(413,321);[why()from() @;mul(647,475)(~}?+-<mul(594,791)mul(713,498)&{mul(19,524)+#when()select()<why()+,]mul(884,220):when()mul(249,82)/~when()!~(@$$ mul(746,775)mul(340,396):+*select()'from()mul(402,793){^mul(760,463)[/<mul(548,103)?'^from()what()&mul(673#/$why(199,312)where(){-mul(226,334)mul(619,629)&mul(742who()$don't()?@}'*>where()<what()select(806,178)mul(783,880);%from()#~*how(28,195)*!mul(387,287)how()@^%[from()mul(393,203)who()--mul(67,670):@when()'{mul(984,238)?when()?;when(141,833)don't()*?>what()what()when()/mul(403,367)when()*@{?]$$mul(883,974)~where():from())why()'-!when()mul;!mul(430,215)*what() '?^}{]what()mul(921,792)[from()when()}what(240,851)mul(792,640)<)^$from()#mul(574,846)$where():[;,mul(543,813)$?]select()mul&[why()mul(550,167)-{$don't()#@[when()mul(439,823),-where()how() [:':*mul(534,346),^mul(781,690)select();@who()'{mul(888,829){(mul(214,861)when(844,270)[from()select()&)&mul(537,154)how(223,646)from()]where(328,122)select()}%<don't(){-mul(801,873)'-,-+^what()#mul(412,143)>^;/]>?)mul(930,63)&,%select()-how()where()~?mul(215,755)*mul(219,137)]how()*select()?%mul(864,539))  #/:/-/mul(179,611)mul(391,430)-mul(913,30)'^ }&mulwhen()who() *mul(46,964)';{how();select()[when()do()[?mul(180,395)@select()select()who()what()don't()select()]'>$mul(290,671)~don't()}*where(14,468)};%what(316,924)?>mul(9,769)where()%,who()'^+&what()@mul(830,738)~!>~>{mul(748,185)]%mul(850,291)>,?+/mul(45,570)#[}who()] mul(164,320)-how():who():mul(46,296);?@-/#;,,don't()why()mul(785,395)?mul(398,117)@mul(340,94)$]select())!:;mul(6,206) *how()($where()<how()#mul(618,791)&#[%:when()>+mul(920,649))><where()don't()from() /(#'/})-mul(808,748)<)what()@+do()who()/*?-mul(207,329);}}'-+#mul(194,625)mul(918,273)$what(620,300)&~~'+)--mulselect(75,131)mul(888,294)-&~mul(189,104))when()mul(225,580)when()( :mul(732,265)?}^)<mul(52,690))&[~-how()mul(134,563)mul(665,473)?from()!,<what()select(437,57):mul(344*what()how()when(512,253)/[*;'?mul(209,717)(select()!!@{how()#mul(896,270),;)<;#}mul(398,671)@'?+$mul(47,963)-what()mul(45,141)-*!why()[why()mul(145,835),$$$select();(mul(795,657)how()@:,mulhow(),mul(706,818)<%mul(149,292)/mul(85,519):)]#!don't() how(782,262)},+:<'where()@mul(884,75);?}why()why() mul(347,632);<where()why()!]~^why()mul(278,913)mul(139&]/!*why(){$+!mul(753,982)mul(587,853),why()why(),select()-)~mul(690,329)when();how()'who()from()<&mul(439,377&'from()'~(mul(514,396) :!$where()!]%^mul(579,128)when()-?who()what()-->%?mul(166,255)where()where():from()mul(271,210)/what(){mul(564,224):mul(513,296)what(404,568)mul(483,797)!?(from()mul(225,16)why())$where()mul(609,630)}]when()(!who(882,295)[what()mul(703,292)mul(816,911)@@ who();mul(272,571)mul(144,283)$~$:;}!>:&mul(691,405)[don't()where()( what()':*]mul(769,350)[?/!<!mul(125,603)+/what()~<where()mul(477,976)mul(936,483)mul(173,66)]/++'~mul(334,249)^$~]who()<-$how()(do()<;mul(983,747)when()when()select()[when();mul(339,465)]>select()(:)+mul(16,661)where()&:^what()select()!mul(724,965)mul(256,462)$>&@,>~what()how(626,774)when()mul(819,930)%!@#%&,$select()mul:select()what()@don't()who()%why()~$&)'?mul(899,128){what(){how()do()!(,):what(381,741)how()mul(626,231)how(941,70)]!why()>[who()^}do()!]~mul(145,559),/?from();/mul(52,260)~where()select()*why()!]who()mul(823,108)from();~}/[how()}[!mul(978,24)when())mul(645,292)}< mul(988,213)-%-who()/*%select()/mul(853,489)~: ):?$why()@mul(551,740): what()mul(388,60)when()~mul(862,379){when()where()%+who()>from(533,522),mul(922,276)
mul(759,151),> ;+&mul(583,470) ,:&mul(915,695)mul(464,234)[$>}how()mul(497,706)where()>(:/?^who()*(mul(613,813)^where()from()]mul(932,777) where()]where()<mul(615,58)why()$#&?mul(919,955):where()mul(955#select()how()when()?select()%>how()mul(119,714)/+@+%mul(135,380)why())mul(427,667)[where()$from()*mul(255,4)how()!>-how()<why()> what()mul(967,813)*{'}+*-^,don't()'{mul(520,847)from()from(){select()<mul(477,859)}&/^ -mul(117,974)+where()why()mul(430,558)*] ()!why(),*mul*)don't()?-^how()mul(834,688)+why()when();;mul(781,493)who()mul(4,212)mul(845,330from()^ when()select()from()where()<$when()*mul(603,397)what(){$mul(160,114)from()mul(425,544) -mul$+where(514,204)&select()]mul(672,590)#don't()[mul(782,479)<)!}?$select()$)(mul(67)!<do()why()mul(68,67)<('#)where()#/+what()mul(225,119) from()(+why()@why()mul(548,198)where()()how()#;do()#mul(382,457)~;how() !?>),#mul(828,292)do() mul(866,185)(}from()from()^[mul(810,863)-'what()do()>(/-,$(mul(10,436)[mul(803,717)@?{[why() @]@^mul(982,590)/(%&$select(728,748)^how()^mul(47,419);mul(781,963)@}mul(67,556) *'~mul(242,786)}&?+why(31,93)>@mul(464,770)<{$$(!mul(814what())where()@who()why(408,863)~mul(160,674)when())mul(590,431)mul(781,931)->from()~[;'^'mul(496,694)>)what()-*why()#;-mul(921,65)@#]+/don't():mul(226,608)where()$!+how()#who()]?select()mul(730,950)@'$[)*$mul(563,45)})-where(){select()]what()don't()+mul(943,235)<}:{}/)mul(146,235));[/who()what()select()/([mul(803,289)[/)why(997,896)mul(816,273)+;/mul(547,981)]~!)[{@}{*mul(86,319)#>[ [why()mul(435,211</how(){] mul(892,307)$^<don't()} *[what()*[mul(82,238)mul(664,87)@:what()];from()mul(919,78)how()#<[~#/mul(746,373)[<-,%select()>*where()<mul(486,412)@<when()>)mul(709,58)>:when()what()mul(456,233)@from())mul(204,587)who()$^'<mul(168,38)from();+*why()@when()mul(683,803)[who(400,167)from()]:how()&~:mul(565,865)%)?mul(745,968)how()'&]mul(604,722)when()mul(921,838)mul(640,543)<@~^&}mul(951,554)mul(256,102):-<:-mul(169,377)>$!mul(378,771)mul(714,865)what()((mul(877,397)select()(mul(731,34)what()<>)*from()^mul(380,614)+@why()/*,mul(475,898)mul(966,798)where()how()/,mul(726,964)when();[do()mul(871,365)[%why(); [why(876,114)don't()!what()@'!$when()[mul(831,147)mul(138,465)*select()/{when()~?from(),mul<! from()[ %mul(243,853)^^'~<why()+^how()mul(664when()]mul(710,612)mul(426,390)don't()~&};why()+@mul(440,273^/why()mul(878,682)$)what()?;why();}mul(262,550how()what()+*<mul(599,369)]mul(315,729)>'where(157,142)what() (do()*&mul(365,834@!{[<%;&[what(886,735) mul(807,79)^@;what()mul(433,788){@:* [!:mul(108,43);*'-^~mul(789,645)+}-mulwhat(){ mul(128,276)*why():how()why()mul(133,271)*;(mul(618,659)~select()]{{}^*mul(638,330)who()$when(674,618)mul(908,588),?&~from()/#why()mul(552,454);*from(),mul(615,472)why()#~<~mul(594,691)-mul(23,914)mul(230,641)/where()mul(63,728)mul(810,461)?mul(569,651)$#mul(822,175)^how(677,189),{{?where():%)mul(213,296)(@why()mul(796select()(+$mul(465,480)from()?/ <%who()?{mul(471,797);{who(),~-mul(596,891)~/?(mul(900,127)[' mul(266,693)%%why(),mul(155,347)mul(2,759)from()%mul(523,244)how()what()>*@mul(277,553)'[]how(836,466)$mul(786,297)#why()^~:mul(205,507);?select()where()from())mul(123,841)how()-what()select()@#{#]'#!/usr/bin/perl(?^select()&#where()mul(387,218)how()why()<from(498,24)#mul(456,185)
$who()why()/how()<mul(7,112)@how(842,109)%,mul(651,794))(when(){?/(!where()mul(459,535)#what(3,96)select()$select()$*/why()from(365,536)mul(627,389)'why();#mul(782,394)}(+how()what();%select()^~mul(678,578);+)mul(955,180)+$@-]don't()from()who(){!mul(624,986)!mul(975,290);-mul(772,846),mul(799,602),$how()mul(768,655)' }+mul(219,916)'$why()mul(115,651)!{mul(446$#]]!?^mul(46,730)how(817,885)@;where()$^(]! mul(474,496)::where():#](#what()&mul(861,240)/(!$({from()*mul(855,388)why()from()$@who(),}~)#mul(463,363)from()what()mul(700,542)!&mulhow(10,603)?from()where()&from()~',do()+;/[mul(200,433)when()select():-!/{?mul(49,444)#where()what()how()+mul(846,858)%%:from()]$how(),mul(476,67)]mul(807,80)what()+^:mul(842,301)!select()how()[mul(732,512)&+(@]mul(948,809)]*why(845,453)!from()'-mul(891,479),!:)mul(182,940) ^select()@ mul(113,15)select()*mul(313,46)select()]),~@<~what()mul(101,941)(mul(323,578)when()&)*from()#from()why()<(mul(54,574)^from()mul(974,166)^where()do(){@!%mul(149,659)what()+mul(544$>select()what()&^>:<*mul(48,9) ^!!select()^}[mul(133,330)?how(571,913)?mul(163,966))?{mul(366,101)#$mulwhy(32,414)>%;<where(660,281):*$mul(223,335)what()where()<*;-mul(398,194)((how() (mul(736,464)where()?!~ ~;'mul(861,392)#(from()^#^,mul(368,351)mul(418,855),from()]from()')>?$^mul(721,586)mul&#*$what()[~ '&<do()~!>mul(375,533)mul(342,13)+!where()'mul(568,71)^]~mul(943,549)}?why(842,232)mul(922,154)select()>$don't()why(999,551)why()mul(781,791),%)select(832,592)]~when()+mul(324,528)$select()-:< ?:+mul(553,150),$<}:$-what()-+mul(932,810)%from(106,776)/ +]<when()+@mul(784,815)~![//mul(759,8)&:#]@?mul(262,429)when()where()#what()mul(501,695))}from()@+^{mul(167,200)why()-who(139,635)select()<?&mul(687,780)who()where()*/@>;mul(83,53)-(,when()<mul(513,865)how()+mul(92,634)why() ,-$]/;mul(490,231)!how()where()who()where()(~mul(49,150)how()}{[>where()mul(115,873){&+mul(357,798){#@mul(876,690)why():mul(148,662)+!%@mul(512[how()];mul(122,41)*when()<mul(633,942)?#{mul(682,83)where()$when()%who()mul(332,158)*:'%!mul(213,207)!select()$mul(412,34)-why()'(where()who()?>who()select()mul(452,727)]<:<?<(*select()mul(300,956)^,/:mul(163,151)#}what()~,who()$>mul(336,312)&(}#^[mul(511*what()??~#(:(mul(97,35)(how()}+(+:mul(22,515)/:;#what(953,388)]mul(880,608)%why(64,210)-]!}from()?*mul(690}from()<~select()?><@ mul(444,747)[who()select():/@from()where()how()who()mul(680,790)*mul(208,716);*[-#from()why()from()]*mul(563,604)^-*mul(176,677)^;how()who()$([]mul(11,556)when(733,129)&//%when(129,614)(&mul(134,249)}{'('?select()select(453,909)mul(342how()'(mul(678,629) >'mul/what()/%mul(6,656)+^~(}how()where()['mul(636,232)'from()mul(409,258)@mul(758,574)<mul(278,508)?why()what(434,228):>mul(721,278)~mul(699,927)<^^?^<*[mul(446where()why()[!when():mul(946,616)@!mul(192select();~@;where(940,901)who()/mul(62,543)^who()!from()from()mul(78,502)-who()%{]&(mul(233,954)mul(163,156)!#]#:,}where()mul(403,223)$#'( ~&&~(mul(509,885)^why()*?:/select()#why()mul(826,143)<what()who()>>mul(804,695)what()from(770,634)why()%how()%&>mul(149,604)>do(),[{mul(441,285)?select()from()]mul(75,868)';mul(118,644)#:[:(*#mul(4,371)$mul(622,537)$&>&#(~/*^mul(857,96)(why();,$how()mul(29,888)){;^;from()*<)mul(741,192))$^ &what()~don't()why()+mul(299,631);[from()what()$/~/mul(540,656)(where(39,548)(what()what()@select(){{'mul(700,74)]when()>mul(382,924)>mul(426,551),mul(919,582)
<%>::mul#}@mul(294,775)^$,from()mul(331,246)&how()mul$&:+@mul(883,736)?from()select() (<^]<mul(759,715)!^,>$$mulwhere()?-;?mul(943,7)$mul(177,555)- mul(513,284)mul(660,648)^-mul(641,291)[%;why()mul(592,514) mul(66,46)how())how()/>what()'+/don't()} ~when()how(264,139),(mul(894,155)>[!what()-mul(901,591)@(mul(916,689) ^/$mul(75,541)how()where(404,116)*-+!mul(832,727)%)^^ #(&^do()](why()mul(740,164);$>*mul(89,249)!}mul(32,185)how()mul(28,824)},select()&>,mul(506,528)%who(){select()(when(763,794)-what()mul(665,939)how()/@[$@when())how()mul(114,937)];when()}#mul(655^]where()$from()mul(706,357)where(512,859)/%$ ?mul(13+}(+where();[->mul(476,267)what()how()when()why()from(321,201)~)!;what()mul(94,991)~[~;;'>(%mul(952,295)%[!>mul(120,25)mul(421,23)&>(,,&who(762,481)-^when()don't(),{mul(371,529)%how(913,59)%?+who() ':don't()mul(474*+*,where()from(116,228)mul(328,38)[*{;;mul(978,96<{}@how(983,94)%:mul(132,147)where(10,901)where() :~@mul(610,431)mul(888,304)select()' from()select()mul(256,81)how()when()why()mul(644,801){,?~<~!select()mul(46,359):]>:;)/,[what()mul(100,505)%$[mul(9,449)*~;,??,mul(522,361)$&}why()-from()>>mul(591,388),?*^select()from())don't()~[*/what()}mul(791,491)who()}]%]mul(249,418)^>+'&mul(352,614}{(;*,what()&what()+what()mul(260,957)when()-+mul(288,562)how()]-who()~]*>%do(){mul(375,414)^mul(251,565)+ (mul(991,687)(mul(352,56)(select()mul(337,520)%:@^-how()-mul(602 what()&who()when()!@<[mul(553,348)what(),mul(548,164)why()when()>[!*'[mul(942,713){why()}~-%@&-<mul(273,911)>+mul(586,995)@,>'(mul(382,494)><$({select(4,131) '-mul(109,2)'<'mul(704,332)why()why()$when()>why()mul(540,890)how()#:(mul(769,655'>how() %/what()where()])mul(582,19)where()>who()mulselect()select()mul(131,795)(mul(232,91)!&-@mul(198,512)+-%don't()>/<]when() [mul(914<>}~<#>]?$mul(312,367)(how()why(){mul(617,443)*/? }&where()select()mul(616,699)mul(701,770)mul(825,157)]when()^mul(392,162)'#&don't():}select()@mul(693,146)#-mul(603,425)!}select()where()@why()-select() when()mul(933,229)@?'<what()>?+mul(884,557)what()]when()}why()mul(847,524)mul(90,328):}why()!mul(81,395)do()when()how())who()}who()when()mul(629,441)& !}); )~mul(692,721)how()#{^@':what(869,405)>mul(608*from()+mul(676,426) />mul(486,902)((/*>,%}what()mul(77,932)^* @%~ mul(488,898)mul(107,555)?select()who()who()when()where();?@;mul(337,733)@mul(480,439)who()how():[#+mul(794,629){%&why()@mul(82,847)+from()^^)!($mul&how()[;select()what()what()(mul(241,602)select(440,433)){/why()who()+^don't()%<mul(520,819)mul(715,711)]who();select() mul(173,853)/,$do()+mul(232,260)who(),who()[)+what()#[mul(972,455)mul(299,267)#}}+%% }@don't()}@#)/@$?!mul(439,959)*:;select()-mul(243,922)what()/mul(689,873)mul(433,493)  $how()&/{%mul(499,885)from()[mul(73,84)[mul(847,551)^/mul(224,731)^)/}}!>$ ^mul(859,377)]when()% do()?{}~?where()mul(720,748)#,'/mul(536,697)where()}}mul(713,265)mul(899,349)why()&who()when(828,656)&/mul(689,501),from()/[^++;'<mul(39,378)]mul(569,666)+]mul(139,26)select()~/}+ !%($mul(662,726)}when(250,970)~%from()^mul(931,993)when(309,204)&!)^don't()<<mul(699,92)!-from()why(981,352),##*:mul(318,597)mul(506,957)+-*from()$from()+*mul(705,539)select()%mul(964,725)~{+/#mul(250,222)+what()why()%mul(307,629)-@+}#from()}mul(823,631),select()]!&where();( mul(810,697)where(267,868)$mul(451,44)how()mul(418,577)
!select(388,624)(mul(248,949) @mul(847,442)-(*[what()+where()>%select()do()*%%[ mul(621,611)mul(670,589)who()who()?@$-+what()%~mul(557,904)<mul(663,396)mul(650,882)mul(866,847)what()(;~' $@when(){mul(558,210)#<where();&]what(52,8)from()!<mul(59who()why()/what(){&~])mul(470,671)~)@'?[what(157,190)# how()mul(273,437)#?(%+mul(953,619)where()#][what()from()~-do()when()% select()>  *:who()mul(820,300)how()>!@/-;:&why()mul(240,283)~>);'mul(444,495)what())mul(742,891)how()'?/from()']don't()%--&!{mul(649,766)<[]'@mul(335,976))&($&}?+how()>mul(989,639), {{$*?%,don't()how()mul(52,7)~[select():@who()mul(612,144)<^what())<!how()mul(910,442)'#from() who()> what()mul(962,579)[%mul(516,604)mul(123,70)(;#mul:select()<},,#:what()mul(796,875)<-{}what()@select(),mul(55,775)]^+why()((mul(959,950);mul(364,829)/$<'&<where(223,718)how()mul(462,706)~how()+mul(323,13)]mul(546,191)-~)mul(801,201)from();!++*mul(64,684)mul(214,18){mul(816,127)}}-when(202,215):why(550,592)mul(689,984)&when()$how()^$select()mul(889,789)from())&who()mul(159,868)]&-#who()mul(219,66)select()^!what()#>,}what()@mul(894,605)who()mul(892,921^why()(/>)why()*$mul(862,234),)$#who()mul(336,132)+how()&how()}-select()don't()>why()mul(759#mul(953,908) select()mul<mul(46,909)?@why()<[mul(387,201)how()};-mul(643,383)?!select()mul(441,779)where()where()#when())/#;}where()mul(527,987)^*!~@'>from(323,14)where()mul(901,400)when()who()':*why()select()?''mul(865,372)@[&~ why()[][mul(580,503)from()%^from()!/<mul(827,837)[!+mul(696,725)+when()who(203,907)<-mul(643,508)@(]{'mul(830,456)[;/+mul(252,290)*mul(146,71):>/*#>#mul(274,231)what()when(770,166)from():& how() when())mul(216,599)when()who()&([mul(851,919)when(),%:($#?<mul(996,943)}[&:<@#when()mul(103,593)mul(321,827),from()select()how()mul(191,945){#what()]mul(144,443)&[)!>mul(649,177)#who(938,710),)mul(928,772)^]''!){<~mul(731,905)where()^what()[mul(310,145)why(250,443)/mul(807,828)mul(501,389)){[how()when()?[mul(637,203)?mul(966,499)&}@][@mul(24,625)~^mul(766,214)mul(836,146)&@ what(){;>)mul(466,455)''!>~'why()mul(253,978)mul(723,145)(@*]%{don't()/}([mul(858,196)[>{,^mul(418,456)how()who(){mul(779,669)/&,when()- how()/~mul(905,147)]#mul(499,880)mul(477,925)}>$[%%who()<mul(735,41))}mul(209,755)where()'))who()mul(625,671)select()who()';what()how()mul(432,686)}]-mul(870,750)}>[,;mul(217,810)mul(344,973)-why()from()^mul(196,594)$mul(560,262)*,select())mul(324,357)what()when()mul(231,72)#from()mul(116,627)how()mul(659,509)+]mul(106,630)#~mul(481,665)?*&$-'mul(150,502)how(){${>#( mul(45,905)where()what()+!mul(701,728))@what()mul(930,711)%[[[mul(168,338)when()'mul(81,753)mul(977,451)!mul(515,907)why()who();-who(189,693)-!{mul(79,142)why()(<where()>mul(670,117)*> mul(301,392)@<{select(471,161){mul(181,97)what()from()^when()@mul(647,950)@mul(16,793)>why();when(375,63)]mul(726,704)$who()where()+select() mul(916,402)*who()<,[where()$:how()mul(499,261)where()+#%why()'%,mul(483,12)&[@(what();:)@@mul(657,770)'>()'@select()!when()mul(965,20)how()
  
"""

result = calculate_sum_with_conditions(text)


print(result)





