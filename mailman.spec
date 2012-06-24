# TODO:
# - are *.po files (beside *.mo) needed in binary package?
Summary:	The GNU Mailing List Management System
Summary(es):	El Sistema de Mantenimiento de listas de GNU
Summary(pl):	System Zarz�dzania Listami Pocztowymi GNU
Summary(pt_BR):	O Sistema de Manuten��o de listas da GNU
Name:		mailman
Version:	2.1.7
Release:	3
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
BuildRequires:	rpmbuild(macros) >= 1.268
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
%pyrequires_eq	python-modules
Provides:	group(mailman)
Provides:	user(mailman)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_queuedir	/var/spool/%{name}
%define		_lockdir	/var/lock/%{name}
%define		_logdir		/var/log/%{name}
%define		_logarchdir	/var/log/archiv/%{name}
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
  modera��o, comandos baseados em e-mail, compiladores (digests),
  etc...
- Uma interface extensiva da Web, personaliz�vel lista a lista.
- Interface de administra��o de lista baseada na Web para *todas* as
  tarefas de tipo de admin.
- Arquivos autom�ticos de estilo hypermail baseado na Web (usando
  pipermail ou outros arquivadores externos), incluindo provis�es para
  arquivos privados.
- Lista de e-mails integrada ao gateway de grupo de not�cias.
- Grupo de not�cias integrado ao gateway de lista de e-mail (baseado
  em consulta... se voc� tiver acesso ao servidor nntp, deve ser f�cil
  conseguir efetuar not�cias baseadas em n�o-consulta->gateway de
  lista de e-mails; envie um e-mail a viega@list.org, eu gostaria de
  ajudar a manter isto e aparecer com instru��es).
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

#%{__make} -C misc

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

sed 's#/usr#mailman /usr#' cron/crontab.in > $RPM_BUILD_ROOT/etc/cron.d/%{name}
sed -e 's#/usr/lib/mailman#%{_libdir}/mailman#g' %{SOURCE2} \
	> $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
sed -e 's#/usr/lib/mailman#%{_libdir}/mailman#g' %{SOURCE2} \
	> $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
sed -e 's#/usr/lib/mailman#%{_libdir}/mailman#g' %{SOURCE3} \
	> $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

mv $RPM_BUILD_ROOT%{_libdir}/%{name}/Mailman/mm_cfg.py $RPM_BUILD_ROOT%{_sysconfdir}
ln -s %{_sysconfdir}/mm_cfg.py $RPM_BUILD_ROOT%{_libdir}/%{name}/Mailman/mm_cfg.py

ln -s %{_sysconfdir}/sitelist.cfg $RPM_BUILD_ROOT%{_var}/lib/mailman/data/sitelist.cfg

cat >> $RPM_BUILD_ROOT%{_sysconfdir}/mm_cfg.py << EOF
DEFAULT_EMAIL_HOST		= 'YOUR.HOST.NAME.HERE'
DEFAULT_URL_HOST		= 'YOUR.HOST.NAME.HERE'
IMAGE_LOGOS			= '/mailman/icons/'
PUBLIC_ARCHIVE_URL		= '/mailman/pipermail/%%(listname)s'
MAILMAN_GROUP			= '%{name}'
MAILMAN_USER			= '%{name}'
#DEFAULT_SERVER_LANGUAGE		= 'pl'

# For available options and their descriptions see:
# %{_libdir}/%{name}/Mailman/Defaults.py
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
%useradd -u 94 -d %{_var}/lib/%{name} -s /bin/false -c "GNU Mailing List Manager" -g mailman mailman

%post
if [ "$1" = "1" ]; then
	%service -q crond restart
fi
%{_libdir}/mailman/bin/update
/sbin/chkconfig --add mailman
if [ -f /var/lock/subsys/mailman ] && [ -d /var/spool/mailman/data ]; then
	ln -sf %{_sysconfdir}/sitelist.cfg /var/spool/mailman/data/sitelist.cfg
fi
%service mailman restart "mailman qrunner daemon"

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

%triggerin -- apache1
%webapp_register apache %{_webapp}

%triggerun -- apache1
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
%{_mandir}/man?/*
%attr(2775,root,mailman) %dir %{_sysconfdir}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(644,root,mailman) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mm_cfg.py
%attr(644,root,mailman) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sitelist.cfg
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
/etc/smrsh/%{name}
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
%{_libdir}/%{name}/Mailman
%{_libdir}/%{name}/bin/p*
%attr(2755,root,mailman) %{_libdir}/%{name}/bin/[!p]*
%attr(2755,root,mailman) %{_libdir}/%{name}/cgi-bin/*
%attr(755,root,mailman) %{_libdir}/%{name}/cron/bumpdigests
%attr(755,root,mailman) %{_libdir}/%{name}/cron/checkdbs
%attr(755,root,mailman) %{_libdir}/%{name}/cron/disabled
%attr(755,root,mailman) %{_libdir}/%{name}/cron/gate_news
%attr(755,root,mailman) %{_libdir}/%{name}/cron/mailpasswds
%attr(755,root,mailman) %{_libdir}/%{name}/cron/nightly_gzip
%attr(755,root,mailman) %{_libdir}/%{name}/cron/senddigests
%{_libdir}/%{name}/cron/crontab.in
%{_libdir}/%{name}/cron/paths.py*
%{_libdir}/%{name}/scripts/*
%{_libdir}/%{name}/icons/*
%attr(2755,root,mailman) %{_libdir}/%{name}/mail/*
%{_libdir}/%{name}/templates/*
%{_libdir}/%{name}/pythonlib/*
%{_libdir}/%{name}/messages/*
%{_libdir}/%{name}/tests/*

%dir %{_var}/lib/%{name}
%dir %{_var}/lib/%{name}/archives
%attr(2771,root,mailman) %dir %{_var}/lib/%{name}/archives/private
%dir %{_var}/lib/%{name}/archives/public
%{_var}/lib/%{name}/data
%dir %{_var}/lib/%{name}/lists
%dir %{_var}/lib/%{name}/spam
%dir %{_queuedir}
%dir %{_lockdir}
%dir %{_logdir}
%dir %{_logarchdir}
%dir %{_piddir}
