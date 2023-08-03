def get_file_path_docx(username: str):
    return f"./static/{username}_resume.docx"

KEYWORDS = {'10',
 'a',
 'acceptance',
 'access',
 'accessibility',
 'adversarial',
 'aggregation',
 'agile',
 'agreement',
 'amazon',
 'analysis',
 'analytics',
 'and',
 'android',
 'angular',
 'ansible',
 'apache',
 'api',
 'apm',
 'app',
 'application',
 'architecture',
 'artificial',
 'as',
 'asp.net',
 'assessment',
 'assurance',
 'auditing',
 'automation',
 'aws',
 'azure',
 'back-end',
 'balancing',
 'behavior-driven',
 'bi',
 'big',
 'bitbucket',
 'blob',
 'blockchain',
 'blue-green',
 'braintree',
 'bug',
 'burn-down',
 'bus',
 'business',
 'c#',
 'canary',
 'chaos',
 'chart',
 'chatops',
 'chef',
 'ci',
 'ci/cd',
 'circleci',
 'classification',
 'climate',
 'cloud',
 'cloud-native',
 'cnn',
 'code',
 'coding',
 'collaboration',
 'compliance',
 'computer',
 'computing',
 'configuration',
 'connect',
 'containerization',
 'continuous',
 'contracts',
 'control',
 'convolutional',
 'coverage',
 'cross-platform',
 'cryptocurrency',
 'cryptography',
 'css',
 'cybersecurity',
 'cycle',
 'cycle)',
 'd3.js',
 'data',
 'database',
 'datadog',
 'debt',
 'deep',
 'delivery',
 'dependency',
 'deployment',
 'design',
 'development',
 'devops',
 'devsecops',
 'distributed',
 'django',
 'docker',
 'documentation',
 'drupal',
 'e-commerce',
 'elasticsearch',
 'elk',
 'engineering',
 'enterprise',
 'entity',
 'esb',
 'ethical',
 'etl',
 'evaluation',
 'event-driven',
 'experience',
 'express.js',
 'extract',
 'faas',
 'feature',
 'file',
 'flags',
 'flutter',
 'frameworks',
 'front-end',
 'ftp',
 'function',
 'functional',
 'game',
 'gan',
 'gateways',
 'gathering',
 'gatling',
 'gatsby',
 'gcp',
 'gdpr',
 'general',
 'generation',
 'generative',
 'generators',
 'git',
 'github',
 'gitlab',
 'google',
 'governance',
 'graphql',
 'hacking',
 'helm',
 'hipchat',
 'html',
 'http',
 'hugo',
 'iaas',
 'iam',
 'identity',
 'iis',
 'incident',
 'infrastructure',
 'injection',
 'integration',
 'integration/continuous',
 'intelligence',
 'interface',
 'inversion',
 'ios',
 'istio',
 'java',
 'javascript',
 'jekyll',
 'jenkins',
 'jira',
 'jmeter',
 'joomla',
 'kafka',
 'kanban',
 'kibana)',
 'kotlin',
 'kubernetes',
 'language',
 'laravel',
 'lean',
 'learning',
 'level',
 'life',
 'load',
 'load)',
 'locust',
 'log',
 'logstash,',
 'machine',
 'magento',
 'management',
 'mercurial',
 'mesh',
 'methodologies',
 'metrics',
 'microservices',
 'microsoft',
 'mining',
 'mob',
 'mobile',
 'mobile-first',
 'model',
 'modeling',
 'mongodb',
 'monitoring',
 'mysql',
 'named',
 'native',
 'natural',
 'ner',
 'network',
 'networks',
 'neural',
 'new',
 'nginx',
 'node.js',
 'nosql',
 'oauth',
 'object-oriented',
 'of',
 'on',
 'openid',
 'optimization',
 'owasp',
 'paas',
 'pagerduty',
 'pair',
 'patterns',
 'payment',
 'paypal',
 'penetration',
 'perforce',
 'performance',
 'php',
 'planning',
 'platform',
 'platforms',
 'postgresql',
 'power',
 'practices',
 'preprocessing',
 'principles',
 'privacy',
 'procedural',
 'processing',
 'programming',
 'protection',
 'protocol',
 'prototyping',
 'puppet',
 'python',
 'quality',
 'rabbitmq',
 'rails',
 'react',
 'reactive',
 'recognition',
 'recurrent',
 'refactoring',
 'regulation)',
 'reinforcement',
 'relational',
 'relic',
 'repositories',
 'requirements',
 'response',
 'responsive',
 'restful',
 'retrospectives',
 'review',
 'rnn',
 'ruby',
 's3',
 'saas',
 'saltstack',
 'scalability',
 'science',
 'scrum',
 'sdlc',
 'secure',
 'security',
 'sentiment',
 'server',
 'serverless',
 'servers',
 'service',
 'service-oriented',
 'servicenow',
 'services',
 'sftp',
 'shopify',
 'sign-on',
 'single',
 'site',
 'sla',
 'slack',
 'smart',
 'smells',
 'soap',
 'software',
 'solid',
 'sonarqube',
 'splunk',
 'sprint',
 'sql',
 'ssl/tls',
 'sso',
 'stack',
 'static',
 'storage',
 'stories',
 'stripe',
 'subversion',
 'svn',
 'swift',
 'systems',
 'tableau',
 'teams',
 'technical',
 'test',
 'test-driven',
 'testing',
 'text',
 'threat',
 'tools',
 'top',
 'tracing',
 'tracking',
 'transfer',
 'transform,',
 'travis',
 'twelve-factor',
 'ui',
 'unity',
 'usability',
 'user',
 'ux',
 'velocity',
 'version',
 'victorops',
 'vision',
 'visualization',
 'vue.js',
 'vulnerability',
 'warehousing',
 'waterfall',
 'web',
 'wireframing',
 'woocommerce',
 'wordpress',
 'writing',
 'xamarin'}