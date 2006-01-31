# TODO:
# - are *.po files (beside *.mo) needed in binary package?
Summary:	The GNU Mailing List Management System
Summary(es):	El Sistema de Mantenimiento de listas de GNU
Summary(pl):	System Zarz±dzania Listami Pocztowymi GNU
Summary(pt_BR):	O Sistema de Manutenção de listas da GNU
Name:		mailman
Version:	2.1.7
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/mailman/%{name}-%{version}.tgz
# Source0-md5:	81ea139ecd24fbd2a85a9185a37df402
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-man-pages.tar.bz2
# Source1-md5:	6b55f9f8051c76961b84a12ed17fc14f
Source2:	%{name}.conf
Source3:	%{name}.init
Source4:	%{name}.sysconfig
Source5:	%{name}.logrotate
# Need to check if it's still useful
#Patch0:		%{name}-xss.patch
Patch1:		%{name}-MM_FIND_GROUP_NAME.patch
Patch2:		%{name}-encoding.patch
Patch3:		%{name}-dont-send-broken-reminder-ugly-hack.patch
Patch4:		%{name}-mailmanctl-status.patch
Patch5:		%{name}-cron.patch
Patch6:		%{name}-python-compile.patch
Patch7:		%{name}-build.patch
Patch8:		%{name}-FHS.patch
URL:		http://www.list.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python >= 2.1
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.202
PreReq:		rc-scripts
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(post,preun):	/sbin/chkconfig
Requires(post):	/bin/hostname
Requires(post):	grep
Requires(postun):	fileutils
Requires(postun):	grep
Requires:	crondaemon
%pyrequires_eq	python-modules
Requires:	smtpdaemon
Requires:	webserver
Provides:	group(mailman)
Provides:	user(mailman)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_configdir	/etc/%{name}
%define		_quedirdir	/var/spool/%{name}
%define		_varmmdir	/var/lib/%{name}
%define		_lockdir	/var/lock/%{name}
%define		_logdir		/var/log/%{name}
%define		_logarchdir	/var/log/archiv/%{name}
%define		_piddir		/var/run/%{name}


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

%prep
%setup -q
#patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
%{__aclocal}
%{__autoconf}

%configure \
	--prefix=%{_varmmdir} \
	--exec-prefix=%{_libdir}/%{name} \
	--with-var-prefix=%{_quedirdir} \
	--with-config-dir=%{_configdir} \
	--with-lock-dir=%{_lockdir} \
	--with-log-dir=%{_logdir} \
	--with-pid-dir=%{_piddir} \
	--with-queue-dir=%{_quedirdir}/qfiles \
	--with-username=%{name} \
	--with-groupname=%{name} \
	--with-mail-gid='mailman' \
	--with-cgi-gid='http' \
	--with-mailhost=localhost.localdomain \
	--with-urlhost=localhost.localdomain \
	--without-permcheck 
%{__make}

#%{__make} -C misc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{cron.d,logrotate.d,httpd/httpd.conf,rc.d/init.d,sysconfig,smrsh},%{_mandir}} \
	$RPM_BUILD_ROOT{%{_varmmdir},%{_quedirdir},%{_quedirdir}/qfiles,%{_configdir},%{_lockdir},%{_logdir},%{_logarchdir},%{_piddir}}

PYTHONPATH=$RPM_BUILD_ROOT%{_varmmdir}:$RPM_BUILD_ROOT%{_varmmdir}/pythonlib/
export PYTHONPATH

%{__make} doinstall \
	prefix=$RPM_BUILD_ROOT%{_varmmdir} \
	exec_prefix=$RPM_BUILD_ROOT%{_libdir}/mailman \
	var_prefix=$RPM_BUILD_ROOT%{_quedirdir} \
	FHS_DIRS=$RPM_BUILD_ROOT

%{__make} install-packages -C misc \
	prefix=$RPM_BUILD_ROOT%{_varmmdir} \
	exec_prefix=$RPM_BUILD_ROOT%{_libdir}/mailman \
	var_prefix=$RPM_BUILD_ROOT%{_quedirdir} \

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

sed 's#/usr#mailman /usr#' cron/crontab.in > $RPM_BUILD_ROOT/etc/cron.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/httpd/httpd.conf/90_%{name}.conf
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

mv $RPM_BUILD_ROOT%{_varmmdir}/Mailman/mm_cfg.py $RPM_BUILD_ROOT%{_configdir}
ln -s %{_configdir}/mm_cfg.py $RPM_BUILD_ROOT%{_varmmdir}/Mailman/mm_cfg.py

cat >> $RPM_BUILD_ROOT%{_configdir}/mm_cfg.py << EOF
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

# Create a link to the wrapper in /etc/smrsh to allow sendmail to run it.
ln -s %{_libdir}/%{name}/mail/%{name} $RPM_BUILD_ROOT/etc/smrsh

# regenerate pyc files with proper paths
find $RPM_BUILD_ROOT -name '*.pyc' -exec rm "{}" ";"
%py_comp $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 94 mailman
%useradd -u 94 -d %{_var}/spool/%{name} -s /bin/false -c "GNU Mailing List Manager" -g mailman mailman

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
	%userremove mailman
	%groupremove mailman
	if [ -f /var/lock/subsys/crond ]; then
		/etc/rc.d/init.d/crond restart
	fi
fi

%triggerpostun -- mailman <= mailman 3:2.0.13-6
if [ -f /var/spool/cron/%{name} ]; then
	crontab -u %{name} -r
fi

%triggerpostun -- mailman < mailman %{epoch}:%{version}-%{release}
%{_var}/lib/mailman/bin/update

%files
%defattr(644,root,root,755)
%doc BUGS FAQ NEWS README README.CONTRIB README.NETSCAPE README.USERAGENT TODO UPGRADING INSTALL
%{_mandir}/man?/*
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) /etc/httpd/httpd.conf/*%{name}.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
/etc/smrsh/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/%{name}
%attr(2775,root,mailman) %dir %{_configdir}
%attr(644,root,mailman) %config(noreplace) %verify(not md5 mtime size) %{_configdir}/mm_cfg.py

%attr(754,root,root) /etc/rc.d/init.d/%{name}

%defattr(644,root,mailman,2775)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/cgi-bin
%dir %{_libdir}/%{name}/mail
%attr(2755,root,mailman) %{_libdir}/%{name}/*/*

%dir %{_varmmdir}
%dir %{_varmmdir}/bin
%dir %{_varmmdir}/cron
%dir %{_varmmdir}/icons
%dir %{_varmmdir}/scripts
%dir %{_varmmdir}/templates
%dir %{_varmmdir}/pythonlib
%dir %{_varmmdir}/messages
%dir %{_varmmdir}/tests

%{_varmmdir}/Mailman
%{_varmmdir}/bin/p*
%attr(2755,root,mailman) %{_varmmdir}/bin/[!p]*
%attr(755,root,root) %{_varmmdir}/cron/*
%{_varmmdir}/scripts/*
%{_varmmdir}/icons/*
%{_varmmdir}/templates/*
%{_varmmdir}/pythonlib/*
%{_varmmdir}/messages/*
%{_varmmdir}/tests/*

%dir %{_quedirdir}
%dir %{_quedirdir}/archives
%attr(2771,root,mailman) %dir %{_quedirdir}/archives/private
%dir %{_quedirdir}/archives/public
%{_quedirdir}/data
%dir %{_quedirdir}/lists
#%dir %{_quedirdir}/logs
%dir %{_quedirdir}/qfiles
%dir %{_quedirdir}/spam
%dir %{_lockdir}
%dir %{_logdir}
%dir %{_logarchdir}
%dir %{_piddir}
