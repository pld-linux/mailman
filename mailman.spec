Summary:	The GNU Mailing List Management System
Summary(es):	El Sistema de Mantenimiento de listas de GNU
Summary(pl):	System Zarz±dzania Listami Pocztowymi GNU
Summary(pt_BR):	O Sistema de Manutenção de listas da GNU
Name:		mailman
Version:	2.0.13
Release:	1
Epoch:		3
License:	GPL
Group:		Applications/System
Source0:	http://prdownloads.sourceforge.net/mailman/%{name}-%{version}.tgz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-man-pages.tar.bz2
Patch0:		%{name}-multimail.patch
Patch1:		%{name}-admin.patch
URL:		http://www.list.org/
Requires(pre):	%{_sbindir}/useradd
Requires(pre):	%{_sbindir}/groupadd
Requires(postun):	%{_sbindir}/userdel
Requires(postun):	%{_sbindir}/groupdel
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

See the Mailman home site for current status, including new releases and 
known problems: http://mailman.sourceforge.net.

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
  moderação, comandos baseados em e-mail, compiladores (digests), etc...
- Uma interface extensiva da Web, personalizável lista a lista.
- Interface de administração de lista baseada na Web para *todas* as
  tarefas de tipo de admin.
- Arquivos automáticos de estilo hypermail baseado na Web (usando
  pipermail ou outros arquivadores externos), incluindo provisões para
  arquivos privados.
- Lista de e-mails integrada ao gateway de grupo de notícias.
- Grupo de notícias integrado ao gateway de lista de e-mail (baseado
  em consulta... se você tiver acesso ao servidor nntp, deve ser fácil
  conseguir efetuar notícias baseadas em não-consulta->gateway de lista
  de e-mails; envie um e-mail a viega@list.org, eu gostaria de ajudar a
  manter isto e aparecer com instruções).
- Detecção e correção inteligente de mensagens retornadas.
- Envio de e-mail em massa rápido e integrado.
- Proteção inteligente contra spam.
- Registro ampliável.
- São possíveis múltiplos donos e moderadores de lista.
- Compiladores (digests) opcionais compatíveis com MIME.
- Informa a partir de qual máquina você se inscreveu, caso esteja no
  domínio correto.

Veja o site do Mailman para saber o estado atual, incluindo novas versões 
e problemas conhecidos: http://mailman.sourceforge.net.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal
%{__autoconf}

FQDN=localhost.localdomain \
URL=localhost.localdomain \
MAIL_GID=12,99,0 \
%configure \
	--prefix=%{_var}/state/mailman \
	--exec-prefix=%{_libdir}/mailman \
	--with-var-prefix=%{_var}/spool/mailman \
	--with-username=%{name} \
	--with-groupname=%{name} \
	--with-mail-gid=mail,nobody,root \
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
echo mailman >> /etc/cron/cron.allow
crontab -u mailman /var/state/mailman/cron/crontab.in

%postun
if [ "$1" = "0" ]; then
        /usr/sbin/userdel       %{name}
        /usr/sbin/groupdel      %{name}
fi

%files
%defattr(644,root,root,755)
%doc BUGS FAQ NEWS README README.LINUX README.EXIM README.SENDMAIL README.QMAIL TODO UPGRADING INSTALL

%attr(2775,mailman,mailman) %dir %{_var}/state/mailman

%attr(2755,root,mailman) %{_var}/state/mailman/bin/[^p]*
%attr(2775,root,mailman) %dir %{_libdir}/mailman
%attr(2775,root,mailman) %dir %{_libdir}/mailman/cgi-bin
%attr(2775,root,mailman) %dir %{_libdir}/mailman/mail
%attr(2755,mailman,mailman) %{_libdir}/mailman/*/*

%attr(2775,mailman,mailman) %{_var}/state/mailman/Mailman
%attr(2775,mailman,mailman) %{_var}/state/mailman/bin/p*
%attr(2775,mailman,mailman) %{_var}/state/mailman/cron
%attr(2775,mailman,mailman) %{_var}/state/mailman/icons
%attr(2775,mailman,mailman) %{_var}/state/mailman/scripts
%attr(2775,mailman,mailman) %{_var}/state/mailman/templates
%attr(2775,mailman,mailman) %dir %{_var}/spool/mailman
%attr(2770,mailman,mailman) %{_var}/spool/mailman/archives/private
%attr(2775,mailman,mailman) %{_var}/spool/mailman/archives/public
%attr(2775,mailman,mailman) %{_var}/spool/mailman/data
%attr(2775,mailman,mailman) %{_var}/spool/mailman/filters
%attr(2775,mailman,mailman) %{_var}/spool/mailman/lists
%attr(2775,mailman,mailman) %{_var}/spool/mailman/locks
%attr(2775,mailman,mailman) %{_var}/spool/mailman/logs
%attr(2775,mailman,mailman) %{_var}/spool/mailman/qfiles
%attr(2775,mailman,mailman) %{_var}/spool/mailman/spam
%{_mandir}/man?/*
