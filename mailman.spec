# TODO:
# - are *.po files (beside *.mo) needed in binary package?
Summary:	The GNU Mailing List Management System
Summary(es):	El Sistema de Mantenimiento de listas de GNU
Summary(pl):	System Zarz±dzania Listami Pocztowymi GNU
Summary(pt_BR):	O Sistema de Manutenção de listas da GNU
Name:		mailman
Version:	2.1.5
Release:	1
Epoch:		3
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tgz
# Source0-md5:	f5f56f04747cd4aff67427e7a45631af
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-man-pages.tar.bz2
# Source1-md5:	6b55f9f8051c76961b84a12ed17fc14f
Source2:	%{name}.conf
Source3:	%{name}.init
Source4:	%{name}.sysconfig
# Need to check if it's still useful
#Patch0:		%{name}-xss.patch
Patch1:		%{name}-MM_FIND_GROUP_NAME.patch
URL:		http://www.list.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python >= 2.1
BuildRequires:	python-devel
PreReq:		rc-scripts
Requires(pre):	/usr/bin/getgid
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/useradd
Requires(pre):	/usr/sbin/groupadd
Requires(postun):	/usr/sbin/userdel
Requires(postun):	/usr/sbin/groupdel
Requires(post,preun):	/sbin/chkconfig
Requires(post):	/bin/hostname
Requires(post):	grep
Requires(postun):	fileutils
Requires(postun):	grep
Requires:	crondaemon
Requires:	python-modules
Requires:	smtpdaemon
Requires:	webserver
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

See the Mailman home site for current status, including new releases
and known problems: http://mailman.sourceforge.net/ .

%description -l es
Mailman -- El sistema de manutención de listas de discusión de la
licencia GNU.

%description -l pl
Mailman -- System Zarz±dzania Listami Pocztowymi GNU -- zosta³
napisany g³ównie w Pythonie. Jego mo¿liwo¶ci to:
- standardowe mo¿liwo¶ci: moderowanie, komendy przesy³ane poczt±,
  digesty itp,
- interfejs WWW konfigurowalny dla ka¿dej listy,
- automatyczny system archiwizowania (z u¿yciem pipermaila lub innego
  zewnêtrznego archiwizera) w³±czaj±c w to odpowiednie zarz±dzanie
  prywatnymi archiwami,
- bramki mail <-> news,
- doskona³y system wykrywania odbiæ i korekcji odbitej poczty,
- system ochrony przed spamem,
- rozszerzone logowanie,
- listy mog± byæ w³asno¶ci± wielu osób oraz moderatorów mo¿e byæ
  kilku.

%description -l pt_BR
O Mailman -- O sistema de gerenciamento de listas de discussão do GNU
-- é um sistema de gerenciamento de listas de discussão escrito em sua
maior parte em Python. Características:

- Maioria das características de lista de discussão padrão, incluindo:
  moderação, comandos baseados em e-mail, compiladores (digests),
  etc...
- Uma interface extensiva da Web, personalizável lista a lista.
- Interface de administração de lista baseada na Web para *todas* as
  tarefas de tipo de admin.
- Arquivos automáticos de estilo hypermail baseado na Web (usando
  pipermail ou outros arquivadores externos), incluindo provisões para
  arquivos privados.
- Lista de e-mails integrada ao gateway de grupo de notícias.
- Grupo de notícias integrado ao gateway de lista de e-mail (baseado
  em consulta... se você tiver acesso ao servidor nntp, deve ser fácil
  conseguir efetuar notícias baseadas em não-consulta->gateway de
  lista de e-mails; envie um e-mail a viega@list.org, eu gostaria de
  ajudar a manter isto e aparecer com instruções).
- Detecção e correção inteligente de mensagens retornadas.
- Envio de e-mail em massa rápido e integrado.
- Proteção inteligente contra spam.
- Registro ampliável.
- São possíveis múltiplos donos e moderadores de lista.
- Compiladores (digests) opcionais compatíveis com MIME.
- Informa a partir de qual máquina você se inscreveu, caso esteja no
  domínio correto.

Veja o site do Mailman para saber o estado atual, incluindo novas
versões e problemas conhecidos: http://mailman.sourceforge.net/ .

%prep
%setup -q
#patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}

%configure \
	--prefix=/var/lib/mailman \
	--exec-prefix=/usr/lib/mailman \
	--with-var-prefix=/var/spool/mailman \
	--without-permcheck \
	--with-username=%{name} \
	--with-groupname=%{name} \
	--with-mail-gid='mailman' \
	--with-cgi-gid='http' \
	--with-mailhost=localhost.localdomain \
	--with-urlhost=localhost.localdomain
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{cron.d,httpd/httpd.conf,mailman,rc.d/init.d,sysconfig},%{_mandir}}

PYTHONPATH=$RPM_BUILD_ROOT/var/lib/mailman/:$RPM_BUILD_ROOT/var/lib/mailman/pythonlib/
export PYTHONPATH

%{__make} doinstall \
	prefix=$RPM_BUILD_ROOT%{_var}/lib/mailman \
	exec_prefix=$RPM_BUILD_ROOT%{_libdir}/mailman \
	var_prefix=$RPM_BUILD_ROOT%{_var}/spool/mailman

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

sed 's#/usr#mailman /usr#' cron/crontab.in > $RPM_BUILD_ROOT/etc/cron.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/httpd/httpd.conf/90_%{name}.conf
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/%{name}

mv $RPM_BUILD_ROOT/var/lib/%{name}/Mailman/mm_cfg.py $RPM_BUILD_ROOT/etc/%{name}
ln -s /etc/%{name}/mm_cfg.py $RPM_BUILD_ROOT/var/lib/%{name}/Mailman/mm_cfg.py

cat >> $RPM_BUILD_ROOT/etc/%{name}/mm_cfg.py << EOF
DEFAULT_EMAIL_HOST		= 'YOUR.HOST.NAME.HERE'
DEFAULT_URL_HOST		= 'YOUR.HOST.NAME.HERE'
IMAGE_LOGOS			= '/mailman/icons/'
PUBLIC_ARCHIVE_URL		= '/mailman/pipermail/%%(listname)s'
MAILMAN_GROUP			= '%{name}'
MAILMAN_USER			= '%{name}'
#DEFAULT_SERVER_LANGUAGE		= 'pl'

# For available options and their descriptions see:
# /var/lib/mailman/Mailman/Defaults.py
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`getgid %{name}`" ]; then
	if [ "`getgid %{name}`" != "94" ]; then
		echo "Error: group %{name} doesn't have gid=94. Correct this before installing %{name}." 1>&2
		exit 1
	fi
else
	echo "Adding group %{name} GID=94"
	/usr/sbin/groupadd -f -g 94 -r %{name}
fi

if [ -n "`id -u %{name} 2>/dev/null`" ]; then
	if [ "`id -u %{name}`" != "94" ]; then
		echo "Error: user %{name} doesn't have uid=94. Correct this before installing %{name}." 1>&2
		exit 1
	fi
else
	echo "Adding user %{name} UID=94"
	/usr/sbin/useradd -u 94 -r -d %{_var}/spool/%{name} -s /bin/false -c "GNU Mailing List Manager" -g %{name} %{name} 1>&2
fi

%post
if [ "$1" = "1" ]; then
	if [ -f /var/lock/subsys/crond ]; then
		/etc/rc.d/init.d/crond restart
	fi
fi
/sbin/chkconfig --add mailman
if [ -f /var/lock/subsys/mailman ]; then
	/etc/rc.d/init.d/mailman restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/mailman start\" to start mailman qrunner daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/mailman ]; then
		/etc/rc.d/init.d/mailman stop 1>&2
	fi
	/sbin/chkconfig --del mailman
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/userdel %{name}
	/usr/sbin/groupdel %{name}
	if [ -f /var/lock/subsys/crond ]; then
		/etc/rc.d/init.d/crond restart
	fi
fi

%triggerpostun -- mailman <= mailman 3:2.0.13-6
if [ -f /var/spool/cron/%{name} ]; then
	crontab -u %{name} -r
fi

%files
%defattr(644,root,root,755)
%doc BUGS FAQ NEWS README README.LINUX README.EXIM README.SENDMAIL README.QMAIL TODO UPGRADING INSTALL
%{_mandir}/man?/*
%attr(640,root,http) %config(noreplace) %verify(not size mtime md5) /etc/httpd/httpd.conf/*%{name}.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/%{name}
%config(noreplace) %verify(not size mtime md5) /etc/cron.d/%{name}
%dir /etc/%{name}
%attr(644,root,mailman) %config(noreplace) %verify(not size mtime md5) /etc/%{name}/mm_cfg.py

%attr(754,root,root) /etc/rc.d/init.d/mailman

%defattr(644,root,mailman,2775)
%dir %{_libdir}/mailman
%dir %{_libdir}/mailman/cgi-bin
%dir %{_libdir}/mailman/mail
%attr(2755,root,mailman) %{_libdir}/mailman/*/*

%dir %{_var}/lib/mailman
%dir %{_var}/lib/mailman/bin
%dir %{_var}/lib/mailman/cron
%dir %{_var}/lib/mailman/icons
%dir %{_var}/lib/mailman/scripts
%dir %{_var}/lib/mailman/templates
%dir %{_var}/lib/mailman/pythonlib
%dir %{_var}/lib/mailman/messages
%dir %{_var}/lib/mailman/tests

%{_var}/lib/mailman/Mailman
%{_var}/lib/mailman/bin/p*
%attr(2755,root,mailman) %{_var}/lib/mailman/bin/[!p]*
%{_var}/lib/mailman/cron/*
%{_var}/lib/mailman/scripts/*
%{_var}/lib/mailman/icons/*
%{_var}/lib/mailman/templates/*
%{_var}/lib/mailman/pythonlib/*
%{_var}/lib/mailman/messages/*
%{_var}/lib/mailman/tests/*

%dir %{_var}/spool/mailman
%dir %{_var}/spool/mailman/archives
%attr(2771,root,mailman) %dir %{_var}/spool/mailman/archives/private
%dir %{_var}/spool/mailman/archives/public
%{_var}/spool/mailman/data
%dir %{_var}/spool/mailman/lists
%dir %{_var}/spool/mailman/locks
%dir %{_var}/spool/mailman/logs
%dir %{_var}/spool/mailman/qfiles
%dir %{_var}/spool/mailman/spam
