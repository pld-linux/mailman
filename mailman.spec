Summary:	The GNU Mailing List Management System
Summary(pl):	System Zarz±dzania Listami Pocztowymi GNU
Name:		mailman
Version:	2.0.8
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.gnu.org/gnu/mailman/%{name}-%{version}.tgz
Patch0:		%{name}-configure.patch
URL:		http://www.list.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python >= 2.1
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
  non-polling based news->mail list gatewaying; email viega@list.org (I'd
  like to help get that going and come up with instructions)
- smart bounce detection and correction
- integrated fast bulk mailing
- smart spam protection
- extensible logging
- multiple list owners and moderators are possible
- optional MIME-compliant digests,
- nice about which machine you subscribed from if you're from the
  right domain,

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

gzip -9nf BUGS FAQ INSTALL NEWS README* TODO UPGRADING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

# PERMISSIONS ARE WRONG. FIXME
%{_var}/state/mailman
%{_libdir}/mailman
%{_var}/spool/mailman
