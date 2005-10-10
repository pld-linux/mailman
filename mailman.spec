# TODO:
# - are *.po files (beside *.mo) needed in binary package?
Summary:	The GNU Mailing List Management System
Summary(es):	El Sistema de Mantenimiento de listas de GNU
Summary(pl):	System Zarz±dzania Listami Pocztowymi GNU
Summary(pt_BR):	O Sistema de Manutenção de listas da GNU
Name:		mailman
Version:	2.1.5
Release:	7.2
Epoch:		5
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tgz
# Source0-md5:	f5f56f04747cd4aff67427e7a45631af
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-man-pages.tar.bz2
# Source1-md5:	6b55f9f8051c76961b84a12ed17fc14f
Source2:	%{name}.conf
Source3:	%{name}.init
Source4:	%{name}.sysconfig
Source5:	%{name}.logrotate
# Need to check if it's still useful
#Patch0:		%{name}-xss.patch
Patch1:		%{name}-MM_FIND_GROUP_NAME.patch
Patch2:		%{name}-pl_fix.patch
Patch3:		%{name}-minus-one-jobs.patch
Patch4:		%{name}-encoding.patch
Patch5:		%{name}-dont-send-broken-reminder-ugly-hack.patch
Patch6:		http://www.list.org/CAN-2005-0202.txt
Patch7:		%{name}-mailmanctl-status.patch
Patch8:		%{name}-cron.patch
Patch9:		%{name}-python-compile.patch
Patch10:	%{name}-build.patch
Patch11:	%{name}-FHS.patch
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
%define		_queuedir	/var/spool/mailman
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
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1
cd Mailman/Cgi/
%patch6 -p0
cd ../../
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
%{__aclocal}
%{__autoconf}

%configure \
	--prefix=%{_libdir}/mailman \
	--exec-prefix=%{_libdir}/mailman \
	--with-var-prefix=/var/lib/mailman \
	--with-config-dir=%{_configdir} \
	--with-lock-dir=%{_lockdir} \
	--with-log-dir=%{_logdir} \
	--with-pid-dir=%{_piddir} \
	--with-queue-dir=%{_queuedir} \
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
install -d $RPM_BUILD_ROOT{/etc/{cron.d,httpd/httpd.conf,rc.d/init.d,sysconfig,smrsh,logrotate.d},%{_mandir}} \
	$RPM_BUILD_ROOT%{_logarchdir}

PYTHONPATH=$RPM_BUILD_ROOT%{_libdir}/mailman/:$RPM_BUILD_ROOT%{_libdir}/mailman/pythonlib/
export PYTHONPATH

%{__make} doinstall \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

install cron/crontab.in $RPM_BUILD_ROOT/etc/cron.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_configdir}/apache.conf
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

mv $RPM_BUILD_ROOT%{_libdir}/%{name}/Mailman/mm_cfg.py $RPM_BUILD_ROOT%{_configdir}
ln -s %{_configdir}/mm_cfg.py $RPM_BUILD_ROOT%{_libdir}/%{name}/Mailman/mm_cfg.py

ln -s %{_configdir}/sitelist.cfg $RPM_BUILD_ROOT%{_var}/lib/mailman/data/sitelist.cfg

cat >> $RPM_BUILD_ROOT%{_configdir}/mm_cfg.py << EOF
DEFAULT_EMAIL_HOST		= 'YOUR.HOST.NAME.HERE'
DEFAULT_URL_HOST		= 'YOUR.HOST.NAME.HERE'
IMAGE_LOGOS			= '/mailman/icons/'
PUBLIC_ARCHIVE_URL		= '/mailman/pipermail/%%(listname)s'
MAILMAN_GROUP			= '%{name}'
MAILMAN_USER			= '%{name}'
#DEFAULT_SERVER_LANGUAGE		= 'pl'

# For available options and their descriptions see:
# %{_libdir}/mailman/Mailman/Defaults.py
EOF

# Create a link to the wrapper in /etc/smrsh to allow sendmail to run it.
ln -s %{_libdir}/%{name}/mail/%{name} $RPM_BUILD_ROOT/etc/smrsh

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 94 mailman
%useradd -u 94 -d %{_var}/lib/%{name} -s /bin/false -c "GNU Mailing List Manager" -g mailman mailman

%post
%{_libdir}/mailman/bin/update
if [ "$1" = "1" ]; then
	if [ -f /var/lock/subsys/crond ]; then
		/etc/rc.d/init.d/crond restart
	fi
fi
/sbin/chkconfig --add mailman
if [ -f /var/lock/subsys/mailman ]; then
	if [ -d /var/spool/mailman/data ]; then
		ln -sf %{_configdir}/sitelist.cfg /var/spool/mailman/data/sitelist.cfg
	fi
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

%triggerin -- apache1 >= 1.3.33-2
%apache_config_install -v 1 -c %{_configdir}/apache.conf

%triggerun -- apache1 >= 1.3.33-2
%apache_config_uninstall -v 1

%triggerin -- apache >= 2.0.0
%apache_config_install -v 2 -c %{_configdir}/apache.conf

%triggerun -- apache >= 2.0.0
%apache_config_uninstall -v 2

%triggerpostun -- mailman <= 3:2.0.13-6
if [ -f /var/spool/cron/%{name} ]; then
	crontab -u %{name} -r
fi

%triggerpostun -- mailman <= 5:2.1.5-7
if [ -f /var/lock/subsys/mailman ]; then
	ln -sf %{_configdir}/sitelist.cfg /var/spool/mailman/data/sitelist.cfg
	/etc/rc.d/init.d/mailman stop 1>&2
	stopped=true
fi
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
%{_libdir}/mailman/bin/update
if [ "x$stopped" = "xtrue" ]; then
	rm -f /var/spool/mailman/data/sitelist.cfg
	/etc/rc.d/init.d/mailman start 1>&2
fi
# Restore apache config
if [ -f /etc/httpd/httpd.conf/90_%{name}.conf.rpmsave ] ; then
	mv -f %{_configdir}/apache.conf{,.rpmnew}
	mv -f /etc/httpd/httpd.conf/90_%{name}.conf.rpmsave %{_configdir}/apache.conf
	echo "%{_configdir}/apache.conf created as %{_configdir}/apache.conf.rpmnew"
fi

%files
%defattr(644,root,root,755)
%doc BUGS FAQ NEWS README README.LINUX README.EXIM README.POSTFIX README.SENDMAIL README.QMAIL README.USERAGENT TODO UPGRADING INSTALL
%{_mandir}/man?/*
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/%{name}
%config(noreplace) %verify(not size mtime md5) /etc/cron.d/%{name}
/etc/smrsh/%{name}
%attr(2775,root,mailman) %dir %{_configdir}
%attr(640,root,http) %config(noreplace) %verify(not size mtime md5) %{_configdir}/apache.conf
%attr(644,root,mailman) %config(noreplace) %verify(not size mtime md5) %{_configdir}/mm_cfg.py
%attr(644,root,mailman) %config(noreplace) %verify(not size mtime md5) %{_configdir}/sitelist.cfg

%attr(754,root,root) /etc/rc.d/init.d/mailman

%defattr(644,root,mailman,2775)
%dir %{_libdir}/mailman
%dir %{_libdir}/mailman/bin
%dir %{_libdir}/mailman/cgi-bin
%dir %{_libdir}/mailman/cron
%dir %{_libdir}/mailman/icons
%dir %{_libdir}/mailman/mail
%dir %{_libdir}/mailman/scripts
%dir %{_libdir}/mailman/templates
%dir %{_libdir}/mailman/pythonlib
%dir %{_libdir}/mailman/messages
%dir %{_libdir}/mailman/tests

%{_libdir}/mailman/Mailman
%{_libdir}/mailman/bin/p*
%attr(2755,root,mailman) %{_libdir}/mailman/bin/[!p]*
%attr(2755,root,mailman) %{_libdir}/mailman/cgi-bin/*
%attr(755,root,mailman) %{_libdir}/mailman/cron/bumpdigests
%attr(755,root,mailman) %{_libdir}/mailman/cron/checkdbs
%attr(755,root,mailman) %{_libdir}/mailman/cron/disabled
%attr(755,root,mailman) %{_libdir}/mailman/cron/gate_news
%attr(755,root,mailman) %{_libdir}/mailman/cron/mailpasswds
%attr(755,root,mailman) %{_libdir}/mailman/cron/nightly_gzip
%attr(755,root,mailman) %{_libdir}/mailman/cron/senddigests
%{_libdir}/mailman/cron/crontab.in
%{_libdir}/mailman/cron/paths.py*
%{_libdir}/mailman/scripts/*
%{_libdir}/mailman/icons/*
%attr(2755,root,mailman) %{_libdir}/mailman/mail/*
%{_libdir}/mailman/templates/*
%{_libdir}/mailman/pythonlib/*
%{_libdir}/mailman/messages/*
%{_libdir}/mailman/tests/*

%dir %{_var}/lib/mailman
%dir %{_var}/lib/mailman/archives
%attr(2771,root,mailman) %dir %{_var}/lib/mailman/archives/private
%dir %{_var}/lib/mailman/archives/public
%{_var}/lib/mailman/data
%dir %{_var}/lib/mailman/lists
%dir %{_var}/lib/mailman/spam
%dir %{_queuedir}
%dir %{_lockdir}
%dir %{_logdir}
%dir %{_logarchdir}
%dir %{_piddir}
