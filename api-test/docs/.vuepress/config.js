module.exports = {
    title: 'Easyun Test Api Docs',
    head: [
        ['link', { rel: 'icon', href: '/favicon.ico' }]
    ],
    themeConfig: {
        base: "README.md/",
        sidebar: [
            "/",
            {
                title: "cloudcontrol_example",
                children: [
                    "cloudcontrolApi/cloudcontrol_example"
                ],
            },
            {
                title: "ec2_instance",
                children: [
                    "cloudcontrolApi/ec2_instance",
                ],
            },
            {
                title: "ec2_security_group",
                children: [
                    "cloudcontrolApi/ec2_security_group",
                ],
            },
            {
                title: "s3_bucket",
                children: [
                    "cloudcontrolApi/s3_bucket",
                ],
            },
            {
                title: "feature divided",
                children: [
                    "featureDivided/datacenter_env",
                ],
            },
            {
                title: "aws cli v2",
                children: [
                    "scriptsRef/aws_cli_v2",
                ],
            },
            {
                title: "ec2 awscli v2",
                children: [
                    "scriptsRef/ec2_awscli_v2",
                ],
            },
            {
                title: "s3 awscli v2",
                children: [
                    "scriptsRef/s3_awscli_v2",
                ],
            },
        ],
        sidebarDepth: 1,
        search: true,
        searchMaxSuggestions: 10,
        lastUpdated: 'Last Updated',
        serviceWorker: {
            updatePopup: true
        }
    },
    footer: "Copyright © 2021 Easyun, All rights reserved.",
}
