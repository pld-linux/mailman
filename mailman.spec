Summary:	The GNU Mailing List Management System
Summary(es):	El Sistema de Mantenimiento de listas de GNU
Summary(pl):	System Zarz�dzania Listami Pocztowymi GNU
Summary(pt_BR):	O Sistema de Manuten��o de listas da GNU
Name:		mailman
Version:	2.0.10
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.gnu.org/gnu/mailman/%{name}-%{version}.tgz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-man-pages.tar.bz2
Patch0:		%{name}-configure.patch
URL:		http://www.list.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python >= 2.1
Requires:	smtpdaemon
Requires:	logrotate
Requires:	python >= 2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mailman -- The GNU Mailing List Management System -- is a mailing list
management system written mostly in Python. Features:
- most standard mailing list features, including: moderation, mail
  based commands, digests, etc...
- an extensive Web interface, customizable on a per-list basis,
- web based list administration interface for *all* admin-type tasks
- automatic Web based hypermail-style archives (using pipermail or
  other external archiver), including provisions for private archives
- integrated mail list to newsgroup gatewaying
- integrated newsgroup to mail list gatewaying (polling-based... if
  you have access to the nntp server, you should be able to easily do
  non-polling based news->mail list gatewaying; email viega@list.org
  (I'd like to help get that going and come up with instructions)
- smart bounce detection and correction
- integrated fast bulk mailing
- smart spam protection
- extensible logging
- multiple list owners and moderators are possible
- optional MIME-compliant digests,
- nice about which machine you subscribed from if you're from the
  right domain,

Veja o site do Mailman para saber o estado atual, incluindo novas
vers�es e problemas conhecidos: http://mailman.sourceforge.net.

%description -l es
Mailman -- El sistema de manutenci�n de listas de discusi�n de la
licencia GNU.

%description -l pl
Mailman -- System Zarz�dzania Listami Pocztowymi GNU -- zosta�
napisany g��wnie w Pythonie. Jego mo�liwo�ci to:
- standardowe mo�liwo�ci: moderowanie, komendy przesy�ane poczt�,
  digesty itp,
- interfejs WWW konfigurowalny dla ka�dej listy,
- automatyczny system archiwizowania (z u�yciem pipermaila lub innego
  zewn�trznego archiwizera) w��czaj�c w to odpowiednie zarz�dzanie
  prywatnymi archiwami,
- bramki mail <-> news,
- doskona�y system wykrywania odbi� i korekcji odbitej poczty,
- system ochrony przed spamem,
- rozszerzone logowanie,
- listy mog� by� w�asno�ci� wielu os�b oraz moderator�w mo�e by�
  kilku.

%description -l pt_BR
O Mailman -- O sistema de gerenciamento de listas de discuss�o do GNU
-- � um sistema de gerenciamento de listas de discuss�o escrito em sua
maior parte em Python. Caracter�sticas:

- Maioria das caracter�sticas de lista de discuss�o padr�o, incluindo:
  modera��o, comandos baseados em e-mail, compiladores (digests), etc...
- Uma interface extensiva da Web, personaliz�vel lista a lista.
- Interface de administra��o de lista baseada na Web para *todas* as
  tarefas de tipo de admin.
- Arquivos autom�ticos de estilo hypermail baseado na Web (usando
  pipermail ou outros arquivadores externos), incluindo provis�es para
  arquivos privados.
- Lista de e-mails integrada ao gateway de grupo de not�cias.
- Grupo de not�cias integrado ao gateway de lista de e-mail (baseado
  em consulta... se voc� tiver acesso ao servidor nntp, deve ser f�cil
  conseguir efetuar not�cias baseadas em n�o-consulta->gateway de lista
  de e-mails; envie um e-mail a viega@list.org, eu gostaria de ajudar a
  manter isto e aparecer com instru��es).
- Detec��o e corre��o inteligente de mensagens retornadas.
- Envio de e-mail em massa r�pido e integrado.
- Prote��o inteligente contra spam.
- Registro ampli�vel.
- S�o poss�veis m�ltiplos donos e moderadores de lista.
- Compiladores (digests) opcionais compat�veis com MIME.
- Informa a partir de qual m�quina voc� se inscreveu, caso esteja no
  dom�nio correto.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
%configure \
	--prefix=%{_var}/state/mailman \
	--exec-prefix=%{_libdir}/mailman \
	--with-var-prefix=%{_var}/spool/mailman \
	--with-username=%{name} \
	--with-groupname=%{name} \
	--with-mail-gid=12 \
	--with-cgi-gid=51 \
	--with-cgi-ext=.cgi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_var}/state/mailman \
	exec_prefix=$RPM_BUILD_ROOT%{_libdir}/mailman \
	var_prefix=$RPM_BUILD_ROOT%{_var}/spool/mailman

install -d $RPM_BUILD_ROOT%{_mandir}
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf BUGS FAQ INSTALL NEWS README* TODO UPGRADING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%dir %{_var}/state/mailman

%attr(755,root,root) %{_var}/state/mailman/bin/[^p]*
%attr(755,root,root) %{_libdir}/mailman

%{_var}/state/mailman/Mailman
%{_var}/state/mailman/bin/p*
%{_var}/state/mailman/cron
%{_var}/state/mailman/icons
%{_var}/state/mailman/scripts
%{_var}/state/mailman/templates
%{_var}/spool/mailman
%{_mandir}/man8/*
