$firewall_args = @{ 
 
    'DisplayName' = 'Adobe_PATCH';
    'Program' = 'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe';
    'Action' = 'Block';
    'Profile' = 'Domain, Private'
    'Description' = 'Fucking test';
    'Protocol' = 'TCP';
    'Direction' = 'Inbound'
     
    }

New-NetFirewallRule @firewall_args