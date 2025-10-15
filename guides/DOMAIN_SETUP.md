# Custom Domain Setup - Complete!

## ✅ Railway Configuration Done

Your custom domains have been configured in Railway:

### Production Environment
- **Custom Domain:** `crm.davethedev.co.nz`
- **Railway Domain:** `django-crm-api-production.up.railway.app`
- **Status:** Configured, waiting for DNS

### Development Environment
- **Custom Domain:** `crm-dev.davethedev.co.nz`
- **Railway Domain:** `django-crm-api-development.up.railway.app`
- **Status:** Configured, waiting for DNS

## 🌐 DNS Records to Add

Log into your DNS provider for `davethedev.co.nz` and add these CNAME records:

### For Production (crm.davethedev.co.nz)
```
Type:  CNAME
Name:  crm
Value: 5ibpu1rb.up.railway.app
TTL:   Auto or 3600
```

### For Development (crm-dev.davethedev.co.nz)
```
Type:  CNAME
Name:  crm-dev
Value: l4ua5q23.up.railway.app
TTL:   Auto or 3600
```

## 📋 Where to Add DNS Records

Depending on where your domain is registered/hosted:

**If using Cloudflare:**
1. Go to Cloudflare Dashboard
2. Select `davethedev.co.nz`
3. Click **DNS** in the left menu
4. Click **Add record**
5. Add both CNAME records above
6. Make sure **Proxy status** is set to **DNS only** (gray cloud, not orange)

**If using another provider:**
1. Log into your domain registrar
2. Find DNS settings / DNS management
3. Add the two CNAME records above

## ⏱️ Propagation Time

- **Minimum:** 5-10 minutes
- **Average:** 30 minutes - 2 hours
- **Maximum:** Up to 72 hours (rare)

## ✅ Environment Variables Updated

Both Railway environments now have:
- ✅ `CSRF_TRUSTED_ORIGINS` - includes both custom and Railway domains
- ✅ `ALLOWED_HOSTS` - includes both custom and Railway domains
- ✅ SSL certificates will be auto-provisioned once DNS propagates

## 🧪 Testing After DNS Propagates

### Check DNS Propagation
```bash
# Check production domain
dig crm.davethedev.co.nz +short

# Check development domain
dig crm-dev.davethedev.co.nz +short

# Or use online tool
https://dnschecker.org/
```

### Test Production
```bash
curl https://crm.davethedev.co.nz/api/companies/
```

### Test Development
```bash
curl https://crm-dev.davethedev.co.nz/api/companies/
```

## 🎉 Once DNS is Live

You can access your CRM at:

**Production (Live):**  
🚀 https://crm.davethedev.co.nz

**Development (Testing):**  
🔧 https://crm-dev.davethedev.co.nz

**Backup URLs (always work):**
- Production: https://django-crm-api-production.up.railway.app
- Development: https://django-crm-api-development.up.railway.app

## 🔒 SSL/HTTPS

Railway automatically provisions and manages SSL certificates for custom domains. Once DNS propagates:
- ✅ Certificate auto-issued (Let's Encrypt)
- ✅ HTTPS automatically enabled
- ✅ HTTP redirects to HTTPS
- ✅ Auto-renewal every 90 days

No action needed on your part!

## 📝 Next Steps

1. **Add DNS records** in your domain provider
2. **Wait 30-60 minutes** for DNS to propagate
3. **Test the domains** using curl or browser
4. **Verify SSL** - should see green padlock in browser
5. **Share the professional URL** with your team/clients!

---

**Summary:**
- ✅ Domains configured in Railway
- ✅ Environment variables updated
- ⏳ Waiting for DNS records to be added
- ⏳ Waiting for DNS propagation (after you add records)
