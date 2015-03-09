using System;
using System.Security.Cryptography;
using System.Text;
namespace WindowsFormsApplication2
{
	public static class Encryption
	{
		public static string Encrypt(string input, string key)
		{
			byte[] bytes = Encoding.UTF8.GetBytes(input);
			TripleDESCryptoServiceProvider tripleDESCryptoServiceProvider = new TripleDESCryptoServiceProvider();
			tripleDESCryptoServiceProvider.Key = Encoding.UTF8.GetBytes(key);
			tripleDESCryptoServiceProvider.Mode = CipherMode.ECB;
			tripleDESCryptoServiceProvider.Padding = PaddingMode.PKCS7;
			ICryptoTransform cryptoTransform = tripleDESCryptoServiceProvider.CreateEncryptor();
			byte[] array = cryptoTransform.TransformFinalBlock(bytes, 0, bytes.Length);
			tripleDESCryptoServiceProvider.Clear();
			return Convert.ToBase64String(array, 0, array.Length);
		}
		public static string Decrypt(string input, string key)
		{
			byte[] array = Convert.FromBase64String(input);
			TripleDESCryptoServiceProvider tripleDESCryptoServiceProvider = new TripleDESCryptoServiceProvider();
			tripleDESCryptoServiceProvider.Key = Encoding.UTF8.GetBytes(key);
			tripleDESCryptoServiceProvider.Mode = CipherMode.ECB;
			tripleDESCryptoServiceProvider.Padding = PaddingMode.PKCS7;
			ICryptoTransform cryptoTransform = tripleDESCryptoServiceProvider.CreateDecryptor();
			byte[] bytes = cryptoTransform.TransformFinalBlock(array, 0, array.Length);
			tripleDESCryptoServiceProvider.Clear();
			return Encoding.UTF8.GetString(bytes);
		}
	}
}
