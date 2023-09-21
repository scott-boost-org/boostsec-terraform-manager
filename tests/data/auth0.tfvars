context = {}

auth0 = {
  domain = "dev-bm7ulkr9.us.auth0.com"
}

boostsec_client_api_audience = "https://api.boostsecurity.dev"

callback_urls = [
  "http://localhost:3000", "https://oauth.pstmn.io/v1/callback",
  "https://app.dev.boostsec.io"
]

allowed_logout_urls = ["http://localhost:3000", "https://app.dev.boostsec.io"]
allowed_web_origins = ["http://localhost:3000", "https://app.dev.boostsec.io"]
initiate_login_uri  = "https://app.dev.boostsec.io/login"

admin_dashboard = {
  callback_urls = [
    "http://localhost:3000", "https://oauth.pstmn.io/v1/callback",
    "https://admin-app.dev.boostsec.io"
  ]
  allowed_logout_urls = ["http://localhost:3000", "https://admin-app.dev.boostsec.io"]
  allowed_web_origins = ["http://localhost:3000", "https://admin-app.dev.boostsec.io"]
  initiate_login_uri  = "https://admin-app.dev.boostsec.io/login"
}

organizations = {
  boost = {
    display_name = "BoostSecurity.io (Dev)"
    boost_org_id = "73661fc0-e406-45aa-8015-16fe84bab025"
    boost_org_features = [
      "cloud-scanning", "config-provisioning", "advanced_policy", "issues", "gitlab_root"
    ]
    branding = {
      logo_url         = "https://docs.boostsecurity.io/assets/logo.png"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connections = {
      google-social = true
      google-boost  = true
    }
    connection_ids = []
    conn_defaults  = false
  },
  entropy = {
    display_name       = "BoostSecurity.io (Dev Entropy)"
    boost_org_id       = "9913811a-640c-40d3-af63-5b41a69a00d2"
    boost_org_features = ["gitlab_root", "advanced_policy"]
    branding = {
      logo_url         = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Figure_06_02_02.jpg?20160705131952"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  jonathan = {
    display_name       = "Jonathan Serafini (Dev)"
    boost_org_id       = "76a175f4-6189-43c2-b846-6d4a86bee303"
    boost_org_features = ["gitlab_root", "cloud-scanning", "config-provisioning", "advanced_policy", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning"]
    branding = {
      logo_url         = "https://avatars.githubusercontent.com/u/736916?v=4"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  sandbox = {
    display_name       = "BoostSecurity.io (Dev Sandbox)"
    boost_org_id       = "765a52f3-c57d-45af-b71b-7e42623082a2"
    boost_org_features = ["gitlab_root", "advanced_policy"]
    branding = {
      logo_url         = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Two_small_test_tubes_held_in_spring_clamps.jpg/440px-Two_small_test_tubes_held_in_spring_clamps.jpg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  zaid = {
    display_name       = "Zaid Boost (Dev)"
    boost_org_id       = "9acadf25-9da7-4e53-82b8-d937c4dc5021"
    boost_org_features = ["gitlab_root", "advanced_policy"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  stephan = {
    display_name       = "Stephan Boost (Dev)"
    boost_org_id       = "48d8653e-b8f0-4f4c-b28c-28a529e29313"
    boost_org_features = ["gitlab_root", "cloud-scanning", "config-provisioning", "advanced_policy", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning", "ecr-integration"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  stephan-doc = {
    display_name       = "Stephan Doc Boost (Dev)"
    boost_org_id       = "e0b71744-e738-4875-9be3-c8a19906b78b"
    boost_org_features = ["gitlab_root", "cloud-scanning", "config-provisioning", "advanced_policy", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  uiux = {
    display_name       = "UX-UI Boost (Dev)"
    boost_org_id       = "9fd072bf-dd1b-4316-9db3-1706b0cdaad1"
    boost_org_features = ["gitlab_root", "advanced_policy"]
    branding = {
      logo_url         = "https://upload.wikimedia.org/wikipedia/commons/3/33/Figma-logo.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  mroy-dev = {
    display_name       = "Martin Boost (Dev)"
    boost_org_id       = "ac7fe5c6-f622-461e-9fe1-7d844aec99a5"
    boost_org_features = ["gitlab_root", "advanced_policy", "cloud-scanning", "config-provisioning", "issues", "gitlab-on-prem", "pipeline-service", "advanced_policy", "azure_devops_provisioning", "ecr-integration"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  amf = {
    display_name       = "Alexis Boost (Dev)"
    boost_org_id       = "e809c889-dec6-49da-b2de-8c181d1c836c"
    boost_org_features = ["gitlab_root", "advanced_policy", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  jake = {
    display_name       = "Jake Boost (Dev)"
    boost_org_id       = "f0b9f4de-022c-460b-8cba-f4eec31765e3"
    boost_org_features = ["gitlab_root", "advanced_policy", "cloud-scanning", "config-provisioning", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning", "ecr-integration"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  dylan = {
    display_name       = "Dylan Boost (Dev)"
    boost_org_id       = "c9989a2e-b9c2-43ef-a763-2ef2eb97091c"
    boost_org_features = ["gitlab_root", "advanced_policy", "config-provisioning", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  victor = {
    display_name       = "Victor Boost (Dev)"
    boost_org_id       = "24e3efdd-b20f-42d6-9102-7d24278321ba"
    boost_org_features = ["gitlab_root", "advanced_policy", "cloud-scanning", "config-provisioning", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning", "ecr-integration"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  sara-dev = {
    display_name       = "Sara Lavanchy (Dev)"
    boost_org_id       = "f3321ca4-c3d9-4349-93e2-75d23e289ad4"
    boost_org_features = ["gitlab_root", "cloud-scanning", "advanced_policy", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning", "ecr-integration"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  thiago-dev = {
    display_name       = "Thiago Boost (Dev)"
    boost_org_id       = "c17b5d1a-776d-5beb-be38-646fa6182a1f"
    boost_org_features = ["gitlab_root", "cloud-scanning", "advanced_policy", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#15803D"
      background_color = "#000000"
    }
    connection_ids = []
  },
  fproulx-dev = {
    display_name       = "François Proulx (Dev)"
    boost_org_id       = "47a1abeb-cf63-423f-ac4f-9921710a5665"
    boost_org_features = ["gitlab_root", "advanced_policy", "cloud-scanning", "config-provisioning", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  benoit-dev = {
    display_name       = "Benoit Cote-Jodoin (Dev)"
    boost_org_id       = "9840022a-9e27-427e-b579-ff8437834e5c"
    boost_org_features = ["gitlab_root", "advanced_policy", "cloud-scanning", "config-provisioning", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  test = {
    display_name       = "Automated Testing Account"
    boost_org_id       = "feaa7ea2-7229-46cc-8063-3a226ff2c110"
    boost_org_features = ["gitlab_root", "cloud-scanning", "config-provisioning", "issues", "gitlab-on-prem", "pipeline-service"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = ["con_vUx0q7rRld39PvLG"] # username password connection for test user
    conn_defaults  = false
  },
  scott-dev = {
    display_name       = "Scott Luu (Dev)"
    boost_org_id       = "3a3dddbc-b2a1-4dd5-a4d5-2693a88bba50"
    boost_org_features = ["gitlab_root", "advanced_policy", "cloud-scanning", "config-provisioning", "gitea", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  olivier-dev = {
    display_name       = "Olivier Leduc (Dev)"
    boost_org_id       = "a4a208f8-77c6-49ab-b3a5-237c88067e96"
    boost_org_features = ["gitlab_root", "cloud-scanning", "config-provisioning", "issues", "gitlab-on-prem", "pipeline-service", "advanced_policy", "azure_devops_provisioning", "ecr-integration"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  leandro-dev = {
    display_name       = "Leandro Correia (Dev)"
    boost_org_id       = "2888a447-dc04-4f6b-9377-fc37a8ebe9cc"
    boost_org_features = ["gitlab_root", "advanced_policy", "cloud-scanning", "config-provisioning", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning", "ecr-integration"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  bao-dev = {
    display_name       = "Bao (Dev)"
    boost_org_id       = "def3380c-84c0-4712-85ad-b73646c6733b"
    boost_org_features = ["gitlab_root", "cloud-scanning", "config-provisioning", "advanced_policy", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning", "ecr-integration"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  mathieu = {
    display_name       = "Mathieu Lemay (Dev)"
    boost_org_id       = "b2fa9632-c877-4ad4-82f3-a0ddf0750eec"
    boost_org_features = ["gitlab_root", "cloud-scanning", "config-provisioning", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning"]
    branding = {
      logo_url         = "https://www.gravatar.com/avatar/75c2c3a84f53d48e3cb1ac857913ee7a"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  pentest-netspi-2023q2-a = {
    display_name       = "NetSPI - 2023 Q2 - A"
    boost_org_id       = "84749589-5ce1-47f4-b9a2-67a5c713017b"
    boost_org_features = []
    branding = {
      logo_url         = "https://www.netspi.com/wp-content/uploads/2021/01/head-logo-1.svg"
      primary_color    = "#ff0028"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  pentest-netspi-2023q2-b = {
    display_name       = "NetSPI - 2023 Q2 - B"
    boost_org_id       = "471da2a3-a415-4051-9002-eafcc9da8c93"
    boost_org_features = []
    branding = {
      logo_url         = "https://www.netspi.com/wp-content/uploads/2021/01/head-logo-1.svg"
      primary_color    = "#ff0028"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  sudocorp = {
    display_name       = "sudocorp"
    boost_org_id       = "f47ccd08-fc71-42b8-b732-c74d5bb7a45e"
    boost_org_features = ["gitlab_root", "config-provisioning", "issues", "advanced_policy", "pipeline-service"]
    branding = {
      logo_url         = "https://pseudocode.deepjain.com/favicon.png"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  good-code = {
    display_name       = "Good Code"
    boost_org_id       = "2df698b4-4358-46b4-8559-693fee158b66"
    boost_org_features = ["gitlab_root", "cloud-scanning", "advanced_policy", "issues", "gitlab-on-prem", "pipeline-service"]
    branding = {
      logo_url         = "https://goodcode.io/static/images/layout/logo-en.png"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  chasen-bettinger = {
    display_name       = "Chasen Bettinger"
    boost_org_id       = "b9c13416-f08e-49c5-b38c-4baee2130267"
    boost_org_features = ["gitlab_root", "advanced_policy"]
    branding = {
      logo_url         = "https://boostsecurity.io/images/programmers-01-1.svg"
      primary_color    = "#141F32"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
  t2g = {
    display_name       = "T2 Test (Dev)"
    boost_org_id       = "ab3b109f-7142-4e52-9333-90c566003b4a"
    boost_org_features = ["gitlab_root", "advanced_policy", "cloud-scanning", "config-provisioning", "issues", "gitlab-on-prem", "pipeline-service", "azure_devops_provisioning"]
    branding = {
      logo_url         = "https://www.gravatar.com/avatar/75c2c3a84f53d48e3cb1ac857913ee7a"
      primary_color    = "#4087c8"
      background_color = "#ffffff"
    }
    connection_ids = []
  },
}
