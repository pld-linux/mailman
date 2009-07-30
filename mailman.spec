#
# Conditional build:
%bcond_with	umbrella_hack	# break anonimization (for use with moderated umbrella list of moderated lists)

%define		rel	5
Summary:	The GNU Mailing List Management System
Summary(es.UTF-8):	El Sistema de Mantenimiento de listas de GNU
Summary(pl.UTF-8):	System Zarządzania Listami Pocztowymi GNU
Summary(pt_BR.UTF-8):	O Sistema de Manutenção de listas da GNU
Name:		mailman
Version:	2.1.11
Release:	%{rel}%{?with_umbrella_hack:.umh}
Epoch:		5
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/mailman/%{name}-%{version}.tgz
# Source0-md5:	d9fd89f54c4743dbcb3b3eec8c6146d6
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-man-pages.tar.bz2
# Source1-md5:	6b55f9f8051c76961b84a12ed17fc14f
Source2:	%{name}.conf
Source3:	%{name}.init
Source4:	%{name}.sysconfig
Source5:	%{name}.logrotate
Source6:	add_nonmembers
Source7:	subscribe_list
Patch0:		%{name}-MM_FIND_GROUP_NAME.patch
Patch1:		%{name}-dont-send-broken-reminder-ugly-hack.patch
Patch2:		%{name}-mailmanctl-status.patch
Patch3:		%{name}-cron.patch
Patch4:		%{name}-python-compile.patch
Patch5:		%{name}-build.patch
Patch6:		%{name}-FHS.patch
Patch7:		%{name}-x-imap-folder.patch
Patch8:		%{name}-lib64.patch
Patch9:		%{name}-umbrella-anon-hack.patch
Patch10:	%{name}-python2.6.patch
Patch11:	%{name}-python2.6-exceptions-quickfix.patch
Patch12:	%{name}-daemonize-fds.patch
Patch13:	%{name}-httpauth.patch
URL:		http://www.list.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python >= 2.1
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.234
Requires(post):	/bin/hostname
Requires(post):	grep
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(postun):	fileutils
Requires(postun):	grep
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	/sbin/chkconfig
Requires:	crondaemon
Requires:	rc-scripts
Requires:	smtpdaemon
Requires:	webapps
Requires:	webserver
Requires:	webserver(indexfile)
%pyrequires_eq	python-modules
Provides:	group(mailman)
Provides:	user(mailman)
# for converting text/html into plain text in default configuration:
Suggests:	lynx
Conflicts:	logrotate < 3.7-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_queuedir	/var/spool/%{name}
%define		_lockdir	/var/lock/%{name}
%define		_logdir		/var/log/%{name}
%define		_logarchdir	/var/log/archive/%{name}
%define		_piddir		/var/run/%{name}

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}

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

%description -l es.UTF-8
Mailman -- El sistema de manutención de listas de discusión de la
licencia GNU.

%description -l pl.UTF-8
Mailman -- System Zarządzania Listami Pocztowymi GNU -- został
napisany głównie w Pythonie. Jego możliwości to:
- standardowe możliwości: moderowanie, komendy przesyłane pocztą,
  digesty itp,
- interfejs WWW konfigurowalny dla każdej listy,
- automatyczny system archiwizowania (z użyciem pipermaila lub innego
  zewnętrznego archiwizera) włączając w to odpowiednie zarządzanie
  prywatnymi archiwami,
- bramki mail <-> news,
- doskonały system wykrywania odbić i korekcji odbitej poczty,
- system ochrony przed spamem,
- rozszerzone logowanie,
- listy mogą być własnością wielu osób oraz moderatorów może być
  kilku.

%description -l pt_BR.UTF-8
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

%package sendmail
Summary:	Sendmail support for mailman
Summary(pl.UTF-8):	Obsługa mailmana dla sendmaila
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description sendmail
This package provides wrapper symlink in /etc/smrsh that allows
sendmail to run mailman.

%description sendmail -l pl.UTF-8
Ten pakiet udostępnia dowiązanie w /etc/smrsh pozwalające sendmailowi
uruchamiać mailmana.

%prep
%setup -q
%patch0 -p1
#patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%{?with_umbrella_hack:%patch9 -p1}
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

# Conflicts with python built-in email package
sed -i -e 's,EMAILPKG=,#EMAILPKG=,g' misc/Makefile.in

install -p %{SOURCE6} %{SOURCE7} contrib

%build
%{__aclocal}
%{__autoconf}

%configure \
	--prefix=%{_libdir}/%{name} \
	--exec-prefix=%{_libdir}/%{name} \
	--with-var-prefix=/var/lib/%{name} \
	--with-config-dir=%{_sysconfdir} \
	--with-lock-dir=%{_lockdir} \
	--with-log-dir=%{_logdir} \
	--with-pid-dir=%{_piddir} \
	--with-queue-dir=%{_queuedir} \
	--with-username=%{name} \
	--with-groupname=%{name} \
	--with-mail-gid='mailman' \
	--with-cgi-gid='http' \
	--with-mailhost=localhost.localdomain \
	--with-urlhost=localhost.localdomain \
	--without-permcheck

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{cron.d,logrotate.d,rc.d/init.d,sysconfig,smrsh},%{_mandir}} \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_logarchdir}}

PYTHONPATH=$RPM_BUILD_ROOT%{_libdir}/%{name}:$RPM_BUILD_ROOT%{_libdir}/%{name}/pythonlib/
export PYTHONPATH

%{__make} doinstall \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install-packages -C misc \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

sed -e 's#/usr/lib/mailman#%{_libdir}/mailman#g' %{SOURCE2} \
	> $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
sed -e 's#/usr/lib/mailman#%{_libdir}/mailman#g' %{SOURCE2} \
	> $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
sed -e 's#/usr/lib/mailman#%{_libdir}/mailman#g' %{SOURCE3} \
	> $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

install cron/crontab.in $RPM_BUILD_ROOT/etc/cron.d/%{name}

install -p contrib/{subscribe_list,add_nonmembers} $RPM_BUILD_ROOT%{_libdir}/%{name}/bin

ln -s %{_sysconfdir}/sitelist.cfg $RPM_BUILD_ROOT%{_var}/lib/mailman/data/sitelist.cfg

cat >> $RPM_BUILD_ROOT%{_sysconfdir}/mm_cfg.py << 'EOF'
DEFAULT_EMAIL_HOST		= 'YOUR.HOST.NAME.HERE'
DEFAULT_URL_HOST		= 'YOUR.HOST.NAME.HERE'
DEFAULT_HOST_NAME		= 'YOUR.HOST.NAME.HERE'
IMAGE_LOGOS			= '/mailman/icons/'
PUBLIC_ARCHIVE_URL		= '/mailman/pipermail/%%(listname)s'
MAILMAN_GROUP			= '%{name}'
MAILMAN_USER			= '%{name}'
VIRTUAL_HOST_OVERVIEW		= Off

#MTA = 'Postfix'
#POSTFIX_STYLE_VIRTUAL_DOMAINS = []

#DEFAULT_SERVER_LANGUAGE = 'pl'

# If value is True, site administrator is trusted from REMOTE_USER CGI variable
# Use this to if you want to use password authentication for site admin.
USE_HTTP_AUTH   = False

# For available options and their descriptions see:
# %{_docdir}/%{name}-%{version}/Defaults.py*
EOF

touch $RPM_BUILD_ROOT%{_sysconfdir}/aliases{,.db}
touch $RPM_BUILD_ROOT%{_sysconfdir}/adm.pw
touch $RPM_BUILD_ROOT%{_var}/lib/mailman/data/last_mailman_version

# Create a link to the wrapper in /etc/smrsh to allow sendmail to run it.
ln -s %{_libdir}/%{name}/mail/%{name} $RPM_BUILD_ROOT/etc/smrsh

# regenerate pyc files with proper paths
find $RPM_BUILD_ROOT -name '*.pyc' | xargs rm -f
%py_comp $RPM_BUILD_ROOT
# save mm_cfg.py from py_postclean
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/Mailman/mm_cfg.{py,pyX}
%py_postclean %{_libdir}/mailman

# must do this after py_postclean
# should we also symlink .pyc? in case commands are ran as root python would create .pyc file
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/Mailman/mm_cfg.pyX $RPM_BUILD_ROOT%{_sysconfdir}/mm_cfg.py
ln -s %{_sysconfdir}/mm_cfg.py $RPM_BUILD_ROOT%{_libdir}/%{name}/Mailman/mm_cfg.py
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/Mailman/mm_cfg.py.dist

rm -f $RPM_BUILD_ROOT%{_mandir}/README-mailman-man-pages
rm -f $RPM_BUILD_ROOT%{_mandir}/diff.arch.8
rm -f $RPM_BUILD_ROOT%{_libdir}/mailman/messages/*/LC_MESSAGES/*.po

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 94 mailman
%useradd -u 94 -d %{_var}/lib/%{name} -s /bin/false -c "GNU Mailing List Manager" -g mailman mailman

%post
if [ "$1" = "1" ]; then
	if hostname=$(hostname -f 2>/dev/null); then
		%{__sed} -i -e "s,YOUR.HOST.NAME.HERE,$hostname," %{_sysconfdir}/mm_cfg.py
	fi

	%service -q crond restart
fi
if [ ! -f %{_sysconfdir}/adm.pw ]; then
	echo 'Run "%{_libdir}/%{name}/bin/mmsitepass" to set site pass.'
fi
if [ ! -d /var/lib/mailman/lists/mailman ]; then
	echo 'Run "%{_libdir}/%{name}/bin/newlist mailman" to setup site-wide mailinglist.'
fi
if [ -f %{_var}/lib/mailman/data/last_mailman_version ]; then
	%{_libdir}/mailman/bin/update
fi
/sbin/chkconfig --add mailman
if [ -f /var/lock/subsys/mailman ] && [ -d /var/spool/mailman/data ]; then
	ln -sf %{_sysconfdir}/sitelist.cfg /var/spool/mailman/data/sitelist.cfg
fi
if [ ! -f %{_sysconfdir}/aliases ]; then
	touch %{_sysconfdir}/aliases{,.db}
	chown root:mailman %{_sysconfdir}/aliases
	chown mailman:mailman %{_sysconfdir}/aliases.db
	chmod 660 %{_sysconfdir}/aliases{,.db}
fi
%service mailman restart "Mailman Qrunner Daemon"

%preun
if [ "$1" = "0" ]; then
	%service mailman stop
	/sbin/chkconfig --del mailman
fi

%postun
if [ "$1" = "0" ]; then
	%userremove mailman
	%groupremove mailman
	%service -q crond restart
fi

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerpostun -- mailman < 1:2.1.7-2.1
if [ -f /var/spool/cron/%{name} ]; then
	crontab -u %{name} -r
fi

if [ -f /var/lock/subsys/mailman ]; then
	ln -sf %{_sysconfdir}/sitelist.cfg /var/spool/mailman/data/sitelist.cfg
	/sbin/service mailman stop 1>&2
	stopped=true
fi

# rescue app configs.
for i in mm_cfg.py sitelist.cfg; do
	if [ -f /etc/%{name}/$i.rpmsave ]; then
		mv -f %{_sysconfdir}/$i{,.rpmnew}
		mv -f /etc/%{name}/$i.rpmsave %{_sysconfdir}/$i
	fi
done

if [ "`getent passwd mailman | cut -d: -f6`" != "%{_var}/lib/%{name}" ]; then
	echo "Fixing passwd entry"
	/usr/sbin/usermod -d %{_var}/lib/%{name} mailman
fi
echo "Moving data from /var/spool/mailman to /var/lib/mailman"
mv -f /var/spool/mailman/archives/private/* %{_var}/lib/mailman/archives/private/
mv -f /var/spool/mailman/archives/public/* %{_var}/lib/mailman/archives/public/
mv -f /var/spool/mailman/data/* %{_var}/lib/mailman/data/
mv -f /var/spool/mailman/lists/* %{_var}/lib/mailman/lists/
mv -f /var/spool/mailman/spam/* %{_var}/lib/mailman/spam/
mv -f /var/spool/mailman/logs/* %{_logdir}/
mv -f /var/spool/mailman/locks/* %{_lockdir}/
mv -f /var/spool/mailman/qfiles/* %{_queuedir}/
# Fix symlinks for public archives
cd %{_var}/lib/mailman/archives/public/
for i in * ; do
	link=$(readlink "$i")
	dn=$(dirname "$link")
	if [ "$dn" = "/var/spool/mailman/archives/private" ]; then
		ln -sf "%{_var}/lib/mailman/archives/private/$i" "$i"
	fi
done
cd -
# Remove empty dirs (DON'T rm -rf here!)
rmdir --ignore-fail-on-non-empty /var/spool/mailman/{archives/{private,public},archives,data,lists,spam,logs,locks,qfiles}
if [ -f %{_var}/lib/mailman/Mailman/mm_cfg.pyc ]; then
	rm -f %{_var}/lib/mailman/Mailman/mm_cfg.pyc
fi
%{_libdir}/mailman/bin/update
if [ "$stopped" = "true" ]; then
	rm -f /var/spool/mailman/data/sitelist.cfg
	/sbin/service mailman start 1>&2
fi

# nuke very-old config location (this mostly for Ra)
if [ -f /etc/httpd/httpd.conf ]; then
	sed -i -e "/^Include.*%{name}.conf/d" /etc/httpd/httpd.conf
fi

# migrate from httpd (apache2) config dir
if [ -f /etc/httpd/%{name}.conf.rpmsave ]; then
	cp -f %{_sysconfdir}/httpd.conf{,.rpmnew}
	mv -f /etc/httpd/%{name}.conf.rpmsave %{_sysconfdir}/httpd.conf
fi

# migrate from httpd (apache2) config dir
if [ -f /etc/httpd/httpd.conf/90_%{name}.conf.rpmsave ]; then
	cp -f %{_sysconfdir}/httpd.conf{,.rpmnew}
	mv -f /etc/httpd/httpd.conf/90_%{name}.conf.rpmsave %{_sysconfdir}/httpd.conf
fi

rm -f /etc/httpd/httpd.conf/90_%{name}.conf
/usr/sbin/webapp register httpd %{_webapp}
%service -q httpd reload

%files
%defattr(644,root,root,755)
%doc BUGS FAQ NEWS README README.CONTRIB README.NETSCAPE README.USERAGENT TODO UPGRADING INSTALL
%doc Mailman/mm_cfg.py.dist Mailman/Defaults.py
%{_mandir}/man?/*
%attr(2775,root,mailman) %dir %{_sysconfdir}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(644,root,mailman) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mm_cfg.py
%attr(664,root,mailman) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mm_cfg.pyc
%attr(644,root,mailman) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sitelist.cfg
%ghost %attr(660,root,mailman) %{_sysconfdir}/aliases
%ghost %attr(660,root,mailman) %{_sysconfdir}/aliases.db
%ghost %attr(640,root,mailman) %{_sysconfdir}/adm.pw
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/%{name}

%attr(754,root,root) /etc/rc.d/init.d/%{name}

%defattr(644,root,mailman,2775)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/bin
%dir %{_libdir}/%{name}/cgi-bin
%dir %{_libdir}/%{name}/cron
%dir %{_libdir}/%{name}/icons
%dir %{_libdir}/%{name}/mail
%dir %{_libdir}/%{name}/scripts
%dir %{_libdir}/%{name}/templates
%dir %{_libdir}/%{name}/pythonlib
%dir %{_libdir}/%{name}/messages
%dir %{_libdir}/%{name}/tests
%dir %{_libdir}/%{name}/Mailman

# move to %{py_sitedir}?
%{_libdir}/%{name}/Mailman/[A-Z_hiv]*.py[co]
%{_libdir}/%{name}/Mailman/mm_cfg.py
%ghost %{_libdir}/%{name}/Mailman/mm_cfg.pyc
%{_libdir}/%{name}/Mailman/Archiver
%{_libdir}/%{name}/Mailman/Bouncers
%{_libdir}/%{name}/Mailman/Cgi
%{_libdir}/%{name}/Mailman/Commands
%{_libdir}/%{name}/Mailman/Gui
%{_libdir}/%{name}/Mailman/Handlers
%{_libdir}/%{name}/Mailman/Logging
%{_libdir}/%{name}/Mailman/MTA
%{_libdir}/%{name}/Mailman/Queue

%{_libdir}/%{name}/bin/*.py[co]
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/add_members
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/add_nonmembers
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/arch
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/b4b5-archfix
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/change_pw
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/check_db
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/check_perms
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/cleanarch
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/clone_member
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/config_list
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/discard
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/dumpdb
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/find_member
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/genaliases
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/inject
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/list_admins
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/list_lists
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/list_members
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/list_owners
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/mailmanctl
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/mmsitepass
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/newlist
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/qrunner
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/rb-archfix
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/remove_members
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/rmlist
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/show_qfiles
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/subscribe_list
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/sync_members
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/transcheck
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/unshunt
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/update
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/version
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/withlist

%attr(2755,root,mailman) %{_libdir}/%{name}/cgi-bin/admin
%attr(2755,root,mailman) %{_libdir}/%{name}/cgi-bin/admindb
%attr(2755,root,mailman) %{_libdir}/%{name}/cgi-bin/confirm
%attr(2755,root,mailman) %{_libdir}/%{name}/cgi-bin/create
%attr(2755,root,mailman) %{_libdir}/%{name}/cgi-bin/edithtml
%attr(2755,root,mailman) %{_libdir}/%{name}/cgi-bin/listinfo
%attr(2755,root,mailman) %{_libdir}/%{name}/cgi-bin/options
%attr(2755,root,mailman) %{_libdir}/%{name}/cgi-bin/private
%attr(2755,root,mailman) %{_libdir}/%{name}/cgi-bin/rmlist
%attr(2755,root,mailman) %{_libdir}/%{name}/cgi-bin/roster
%attr(2755,root,mailman) %{_libdir}/%{name}/cgi-bin/subscribe

%attr(755,root,root) %{_libdir}/%{name}/cron/bumpdigests
%attr(755,root,root) %{_libdir}/%{name}/cron/checkdbs
%attr(755,root,root) %{_libdir}/%{name}/cron/cull_bad_shunt
%attr(755,root,root) %{_libdir}/%{name}/cron/disabled
%attr(755,root,root) %{_libdir}/%{name}/cron/gate_news
%attr(755,root,root) %{_libdir}/%{name}/cron/mailpasswds
%attr(755,root,root) %{_libdir}/%{name}/cron/nightly_gzip
%attr(755,root,root) %{_libdir}/%{name}/cron/senddigests
%{_libdir}/%{name}/cron/crontab.in
%{_libdir}/%{name}/cron/paths.py*
%{_libdir}/%{name}/scripts/*
%{_libdir}/%{name}/icons/*
%attr(2755,root,mailman) %{_libdir}/%{name}/mail/mailman
%{_libdir}/%{name}/templates/*
%{_libdir}/%{name}/pythonlib/*
%{_libdir}/%{name}/messages/*
%{_libdir}/%{name}/tests/*

%dir %{_var}/lib/%{name}
%dir %{_var}/lib/%{name}/archives
%dir %attr(2771,root,mailman) %{_var}/lib/%{name}/archives/private
%dir %{_var}/lib/%{name}/archives/public
%dir %{_var}/lib/%{name}/data
%ghost %{_var}/lib/%{name}/data/last_mailman_version
%{_var}/lib/%{name}/data/sitelist.cfg
%dir %{_var}/lib/%{name}/lists
%dir %{_var}/lib/%{name}/spam
%dir %{_queuedir}
%dir %{_lockdir}
%dir %{_logdir}
%dir %{_logarchdir}
%dir %{_piddir}

%files sendmail
%defattr(644,root,root,755)
/etc/smrsh/%{name}
